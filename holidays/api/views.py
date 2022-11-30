from django.shortcuts import render
from api.serializer import HolidaySerializer,UserSerializer
from api.models import Holiday
from api.serializer import Holiday
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

class HolidayView(ViewSet):
    def create(self, request, *args, **kwargs):
        serializer = HolidaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    #
    def list(self, request, *args, **kwargs):
        holi = Holiday.objects.all()
        serializer = HolidaySerializer(holi, many=True)
        return Response(data=serializer.data)

    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        holi = Holiday.objects.get(id=id)
        serializer = HolidaySerializer(lev, many=False)
        return Response(data=serializer.data)

    def update(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        instance = Holiday.objects.get(id=id)
        serializer = HolidaySerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        holi = Holiday.objects.get(id=id)
        holi.delete()
        return Response({"msg": "holiday deleted"})
# Create your views here.
