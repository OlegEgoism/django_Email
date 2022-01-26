from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

class UserRegisterationsSerializer(serializers.ModelSerializer):
    # check_password = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User(username=self.validated_data['username'],
                    email=self.validated_data['email'])
        user.set_password(self.validated_data['password'])
        user.save()
        return user

