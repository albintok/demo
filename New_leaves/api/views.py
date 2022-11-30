from django.shortcuts import render
from api.models import Leaves
from api.serializers import LeaveSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# Create your views here.

class Signup(ViewSet):
    def create(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class LeaveView(ViewSet):
    def create(self, request, *args, **kwargs):
        serializer = LeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    #
    # def list(self, request, *args, **kwargs):
    #     lev = Leaves.objects.all()
    #     serializer = LeaveSerializer(emp, many=True)
    #     return Response(data=serializer.data)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     id = kwargs.get("pk")
    #     lev = Leaves.objects.get(id=id)
    #     serializer = LeaveSerializer(lev, many=False)
    #     return Response(data=serializer.data)
    #
    # def update(self, request, *args, **kwargs):
    #     id = kwargs.get("pk")
    #     instance = Leaves.objects.get(id=id)
    #     serializer = LeaveSerializer(instance=instance, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        lev = Leaves.objects.get(id=id)
        lev.delete()
        return Response({"msg": "lev deleted"})
# Create your views here.
