from rest_framework import serializers
from profiles.models import ProfileModel
from core.models import CustomAuthUserModel


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomAuthUserModel
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        print(validated_data)
        auth_user = CustomAuthUserModel.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return auth_user


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=CustomAuthUserModel.objects.all(),
        many=False,
        read_only=False,
        slug_field='userId'
    )

    class Meta:
        model = ProfileModel
        fields = ['name', 'user']

    def to_representation(self, instance):
        print(instance)
        return super().to_representation(instance)

    def validate(self, attrs):
        print(attrs)
        return super().validate(attrs)

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)
