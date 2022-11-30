from api.models import Cakes
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password"]

    def create(self,validated_data):
          return User.objects.create_user(**validated_data)

class CakeSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    id=serializers.CharField(read_only=True)
    created_date=serializers.DateTimeField(read_only=True)
    class Meta:
        model=Cakes
        fields="__all__"

    def create(self,validated_data):
        user=self.context.get("user")
        return Cakes.objects.create(**validated_data,user=user)