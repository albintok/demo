from api.models import Leaves
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["email","username","password"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Leaves
        fields="__all__"

    def create(self, validated_data):
        return Leaves.objects.create(**validated_data)