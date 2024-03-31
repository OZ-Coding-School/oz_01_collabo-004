from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'password', 'name', 'email', 'phone']

    def create(self, validated_data):
        if not validated_data['user_id']:
            raise ValueError('Users must have an user_id')

        user = User(
            user_id=validated_data['user_id'],
            name=validated_data['name'],
            email=validated_data['email'],
            phone=validated_data['phone']
            )
        user.set_password(validated_data['password'])
        user.save()

        return user
    

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'name', 'email', 'phone']

class UserInfoModifySerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'phone', 'password']

    def update(self, instance, validated_data):
        if validated_data:
            password = validated_data.pop('password', None)
            if password is not None:
                instance.set_password(password)  # 비밀번호를 해시화하여 저장
        return super().update(instance, validated_data)

class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['is_active', 'del_req_time']
