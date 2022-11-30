from django.shortcuts import render,redirect
from api.models import Restuarents,Buys,Dishes
from rest_framework import authentication,permissions
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from api.serializers import UserSerializer,BuySerializer,DishSerializer,RestSerializer

from rest_framework.decorators import action

# Create your views here.

# localhost:8000/user/signup/
class UserView(ViewSet):
    def create(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

# # localhost:8000/rests/
# class RestView(ViewSet):
#     authentication_classes =[authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
    # def create(self,request,*args,**kwargs):
    #     user=request.user
    #     serializer=RestSerializer(data=request.data,context={"usr":user})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)
    # def list(self,request,*args,**kwargs):
    #     rst=Restuarents.objects.all()
    #     serializer=(rst,many=True)
    #     return Response(data=serializer.data)
    #
    # def retrieve(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     rst=Restuarents.objects.get(id=id)
    #     serializer=RestSerializer(rst)
    #     return Response(data=serializer.data)
    #
    # def update(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     instance=Restuarents.objects.get(id=id)
    #     serializer=RestSerializer(instance=instance,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)
    # def destroy(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     rst=Restuarents.objects.get(id=id)
    #     rst.delete()
    #     return Response({"msg":"deleted"})

# localhost:8000/rests/
class RestView(ModelViewSet):
    serializer_class = RestSerializer
    queryset = Restuarents.objects.all()
    authentication_classes =[authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user=request.user
        serializer=RestSerializer(data=request.data,context={"user":user})
        if serializer.is_valid():
            serializer.save()
            return  Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



#localhost:8000/rests/{id}/add_dish
    @action(methods=["POST"],detail=True)
    def add_dish(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        user=request.user
        rst=Restuarents.objects.get(id=id)
        serilizer=DishSerializer(data=request.data,context={"user":user,"rest":rst})
        if serilizer.is_valid():
            serilizer.save()
            return Response(data=serilizer.data)
        else:
            return Response(data=serilizer.errors)

#localhost:8000/rests/{id}/get_dishes
    @action(methods=["GET"],detail=True)
    def get_dishs(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        rst=Restuarents.objects.get(id=id)
        dish=rst.dishes_set.all()
        serializer=DishSerializer(dish,many=True)
        return Response(data=serializer.data)


# localhost:8000/rests/most_rated
#     @action(methods=["GET"],detail=False)
#     def most_rated(self, request, *args, **kwargs):
#         rests=Restuarents.objects.all()
#         mst_rated=max(rests,key=lambda rest:len(rest.get("rating")))
#         serializer=RestSerializer(mst_rated,many=False)
#         return Response(serializer.data)

class DishView(ViewSet):
    serializer_class = DishSerializer
    queryset = Dishes.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


 # localhost:8000/dishs/
    def list(self,request,*args,**kwargs):
        all_dishs=Dishes.objects.all()
        serilaizer=DishSerializer(all_dishs,many=True)
        return Response(data=serilaizer.data)

 # localhost:8000/dishs/{id}
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        dish=Dishes.objects.get(id=id)
        serializer=DishSerializer(dish,many=False)
        return Response(data=serializer.data)

 # localhost:8000/dishs/{id}
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        instance=Dishes.objects.get(id=id)
        serializer=DishSerializer(instance=instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

 # localhost:8000/dishs/{id}
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        dish=Dishes.objects.get(id=id)
        dish.delete()
        return Response({"msg":"product deleted"})

 # localhost:8000/dishs/highest_priced
 #    @action(methods=["GET"], detail=False)
 #    def highest_priced(self, request, *args, **kwargs):
 #        dishs = Dishes.objects.all()
 #        print(dishs)
 #        high_price = max(dishs,key=lambda dish:len(dish.get("price")))
 #        serializer = DishSerializer(high_price, many=False)
 #        return Response(serializer.data)

 #localhost:8000/dishs/{id}/add_to_buy
    @action(methods=["POST"],detail=True)
    def add_to_buy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        user=request.user
        dish=Dishes.objects.get(id=id)
        serilizer=BuySerializer(data=request.data,context={"user":user,"dish":dish})
        if serilizer.is_valid():
            serilizer.save()
            return Response(data=serilizer.data)
        else:
            return Response(data=serilizer.errors)

class BuyView(ViewSet):
    serializer_class = BuySerializer
    queryset = Buys.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

 # localhost:8000/buys/{id}
    def list(self,request,*args,**kwargs):
        all_buys=Buys.objects.all()
        serilaizer=BuySerializer(all_buys,many=True)
        return Response(data=serilaizer.data,)


 # localhost:8000/buys/{id}
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        buy=Buys.objects.get(id=id)
        serializer=BuySerializer(buy,many=False)
        return Response(data=serializer.data)

 # localhost:8000/buys/{id}
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        buy=Buys.objects.get(id=id)
        buy.delete()
        return Response({"msg":"Dish removed"})

