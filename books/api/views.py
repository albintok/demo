from django.shortcuts import render
from api.models import Books,BookDetail
from api.serializer import UserSerializer,BookSerializer,BookDetailSerializer
from rest_framework import authentication,permissions
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
class Signup(ViewSet):
    def create(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

# localhost:8000/books/
class BookView(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Books.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]


# localhost:8000/bookdetail/
class BookDetailView(ViewSet):
    authentication_classes =[authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def create(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        user=request.user
        buk=Books.objects.get(id=id)
        serializer=BookDetailSerializer(data=request.data,context={"book":buk})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        bk=Books.objects.get(id=id)
        serializer=BookDetailSerializer(bk)
        return Response(data=serializer.data)

    def update(self, request,*args,**kwargs):
        id=kwargs.get("pk")
        instance=Books.objects.get(id=id)
        serializer=BookDetailSerializer(instance=instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



