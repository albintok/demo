from django.shortcuts import render
from api.serializers import ProjectSerializer,UserSerializer
from api.models import Project
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

class ProjectView(ViewSet):
    def create(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def list(self, request, *args, **kwargs):
        prjt = Project.objects.all()
        serializer = ProjectSerializer(prjt, many=True)
        return Response(data=serializer.data)

    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        prjt = Project.objects.get(id=id)
        serializer = ProjectSerializer(prjt, many=False)
        return Response(data=serializer.data)

    def update(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        instance = Project.objects.get(id=id)
        serializer = ProjectSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        prjt = Project.objects.get(id=id)
        prjt.delete()
        return Response({"msg": "project deleted"})
# Create your views here.

# Create your views here.
