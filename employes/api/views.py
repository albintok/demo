from django.shortcuts import render
from api.models import Employe
from api.serializers import EmployeSerializer,UserSerializer
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

class EmployeView(ViewSet):
    def create(self, request, *args, **kwargs):
        serializer = EmployeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def list(self, request, *args, **kwargs):
        emp = Employe.objects.all()
        serializer = EmployeSerializer(emp, many=True)
        return Response(data=serializer.data)

    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        emp = Employe.objects.get(id=id)
        serializer = EmployeSerializer(emp, many=False)
        return Response(data=serializer.data)

    def update(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        instance = Employe.objects.get(id=id)
        serializer = EmployeSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        emp = Employe.objects.get(id=id)
        emp.delete()
        return Response({"msg": "employe deleted"})