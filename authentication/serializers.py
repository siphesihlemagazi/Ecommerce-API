from rest_framework import serializers
from authentication.models import User


class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']

        read_only_fields = ['token']
