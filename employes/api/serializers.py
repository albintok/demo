from api.models import Employe
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["email","username","password"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employe
        fields="__all__"

    def create(self, validated_data):
        return Employe.objects.create(**validated_data)