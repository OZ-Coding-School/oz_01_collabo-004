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
        fields = ["user_id", "password", "name", "email", "phone", "profile_image"]

    def create(self, validated_data):
        if not validated_data["user_id"]:
            raise ValueError("Users must have an user_id")

        user = User(
            user_id=validated_data["user_id"],
            name=validated_data["name"],
            email=validated_data["email"],
            phone=validated_data["phone"],
        )
        user.set_password(validated_data["password"])
        user.save()

        return user


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["user_id", "name", "email", "phone", "profile_image"]


class UserInfoModifySerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "phone", "password", "profile_image"]

    def update(self, instance, validated_data):
        if validated_data:
            password = validated_data.pop("password", None)
            if password is not None:
                instance.set_password(password)  # 비밀번호를 해시화하여 저장
        return super().update(instance, validated_data)


class VerificationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        email = data.get("email")
        code = data.get("code")
        verification_code = cache.get(f"{email}-verify_code")
        if verification_code is None:
            raise serializers.ValidationError("Email Verification time has expired.")
        if code != verification_code:  # 인증코드 일치 여부 확인
            raise serializers.ValidationError("Invalid verification code")

        return data


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, max_length=30)
