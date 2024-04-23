from django.core.cache import cache
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["user_id", "password", "name", "nickname", "email", "phone", "profile_image"]

    def create(self, validated_data):
        if not validated_data["user_id"]:
            raise ValueError("Users must have an user_id")

        user = User(
            user_id=validated_data["user_id"],
            name=validated_data["name"],
            nickname=validated_data["nickname"],
            email=validated_data["email"],
            phone=validated_data["phone"],
        )
        user.set_password(validated_data["password"])
        user.save()

        return user


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["user_id", "nickname", "name", "email", "phone", "profile_image"]


class UserInfoModifySerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["nickname", "email", "phone", "password", "profile_image"]

    def update(self, instance, validated_data):
        if validated_data:
            password = validated_data.pop("password", None)
            if password is not None:
                instance.set_password(password)  # 비밀번호를 해시화하여 저장
        return super().update(instance, validated_data)


class VerificationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)
    verification_type = serializers.CharField(max_length=15)
    user_id = serializers.CharField(max_length=15, required=False)

    def validate(self, data):
        email = data["email"]
        code = data["code"]
        verification_type = data["verification_type"]

        # 캐시에서 검색하는 키를 설정
        if verification_type == "signup":
            cache_key = f"{email}-verify_code"
        elif verification_type == "forgot_password" and "user_id" in data:
            user_id = data["user_id"]
            cache_key = f"{user_id}-{email}-verify_code"
        else:
            raise serializers.ValidationError("Invalid verification type")

        # 캐시에서 검색한 코드 가져오기
        verification_code = cache.get(cache_key)

        if verification_code is None:
            raise serializers.ValidationError("Email Verification time has expired.")
        if code != verification_code:  # 인증코드 일치 여부 확인
            raise serializers.ValidationError("Invalid verification code")

        return data


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, max_length=30)

    def validate(self, data):
        email = data.get("email", "")
        if not email:
            raise serializers.ValidationError("이메일을 입력해주세요.")
        elif User.objects.filter(email=email).exists():
            raise serializers.ValidationError("이미 가입된 이메일입니다.")
        return data

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=30)
    user_id = serializers.CharField(max_length=15)

    def validate(self, data):
        email = data.get("email")
        if not email:
            raise serializers.ValidationError("이메일을 입력해주세요.")
        user_id = data.get("user_id")
        if not user_id:
            raise serializers.ValidationError("아이디를 입력해주세요.")
        user = User.objects.filter(email=email, user_id=user_id).first()
        if not user:
            raise serializers.ValidationError("입력한 아이디와 이메일 인증정보가 일치하지 않습니다.")
        return data
