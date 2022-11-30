from rest_framework import serializers
from api.models import Restuarents,Dishes,Buys
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["username","password"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
class RestSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    review_count=serializers.CharField(read_only=True)
    class Meta:
        model=Restuarents
        fields="__all__"
    def create(self, validated_data):
        user=self.context.get("user")
        return Restuarents.objects.create(**validated_data,user=user)


class DishSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    restuarent=serializers.CharField(read_only=True)
    class Meta:
        model=Dishes
        fields="__all__"
    def create(self, validated_data):
        user=self.context.get("user")
        restuarent=self.context.get("rest")
        return Dishes.objects.create(**validated_data,user=user,restuarent=restuarent)


class BuySerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)

    class Meta:
        model=Buys
        fields="__all__"
    def create(self, validated_data):
        user=self.context.get("user")
        name=self.context.get("dish")
        return Buys.objects.create(**validated_data,user=user,name=name)