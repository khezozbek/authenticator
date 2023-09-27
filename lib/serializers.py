from .models import Password
from django.contrib.auth.models import User
from rest_framework import serializers


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

    def create(self, validated_data):
        password = validated_data['password']
        password2 = validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user = User(username=validated_data['username'])
        user.set_password(password)
        user.save()
        return user


class PasswordSerializers(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = '__all__'
