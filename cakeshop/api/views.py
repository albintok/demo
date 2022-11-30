from django.shortcuts import render
from api.models import Cakes
from django.contrib.auth.models import User
from api.serializers import UserSerializer,CakeSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework.decorators import action


# Create your views here.
class UserSignupView(ViewSet):
    def create(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class CakeView(ViewSet):
    permission_classes = [permissions.IsAdminUser]

    def create(self,request,*args,**kwargs):
        user=request.user
        serializer=CakeSerializer(data=request.data,context={"user":user})
        if serializer.is_valid():
            serializer.save()
            return  Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def list(self,request,*args,**kwargs):
        all_CAKES=Cakes.objects.all()
        serilaizer=CakeSerializer(all_CAKES,many=True)
        return Response(data=serilaizer.data)


    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cake=Cakes.objects.get(id=id)
        serializer=CakeSerializer(cake,many=False)
        return Response(data=serializer.data)

    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        instance=Cakes.objects.get(id=id)
        serializer=CakeSerializer(instance=instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        cake=Cakes.objects.get(id=id)
        cake.delete()
        return Response({"msg": "cAKE deleted"})

class Userview(ViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        all_CAKES = Cakes.objects.all()
        serilaizer = CakeSerializer(all_CAKES, many=True)
        return Response(data=serilaizer.data)