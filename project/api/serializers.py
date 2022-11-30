from api.models import Project
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["email","username","password"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields="__all__"

    def create(self, validated_data):
        return Project.objects.create(**validated_data)