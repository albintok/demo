from  rest_framework import serializers
from api.models import Books,BookDetail
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["email","username","password"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class BookSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Books
        exclude=["is_active"]
    def create(self, validated_data):
        return Books.objects.create(**validated_data)

class BookDetailSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    book=serializers.CharField(read_only=True)
    like_count=serializers.CharField(read_only=True)
    class Meta:
        model=BookDetail
        fields="__all__"
    def create(self, validated_data):
        user=self.context.get("user")
        book=self.context.get("book")
        return BookDetail.objects.create(**validated_data,user=user,book=book)