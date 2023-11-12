from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import authentication
from rest_framework import permissions

from api.serializers import UserSerializers,CakeOccationSerializer,CakeVarientSerializer,CartSerializer,OrderSerializer

from cake.models import CakeOccation,CakeVarient,CakeCart,CakeOrder
# Create your views here.

class UserCreationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class OccationView(ModelViewSet):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=CakeOccationSerializer
    model=CakeOccation
    queryset=CakeOccation.objects.all()

    #custom method for add to cart
    @action(methods=["post"],detail=True)
    def add_cart(self,request,*args,**kwargs):
        vid=kwargs.get("pk")
        obj=CakeVarient.objects.get(id=vid)
        user=request.user
        serializer=CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(username=user,cakename=obj)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
    @action(methods=["post"],detail=True)
    def place_order(self,request,*args,**kwargs):
        vid=kwargs.get("pk")
        obj=CakeVarient.objects.get(id=vid)
        user=request.user
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cakename=obj,username=user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class CartView(ViewSet):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=CartSerializer

    def list(self,request,*args,**kwargs):
        qs=CakeCart.objects.filter(username=request.user)
        serializer=CartSerializer(qs,many=True)
        return Response(data=serializer.data)
    

    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        instance=CakeCart.objects.get(id=id)
        if instance.username==request.user:
            instance.delete()
            return Response(data={"msg":"deleted"})
        else:
            return Response(data={"msg":"permission denied"})
class OrderView(ViewSet):
    #authentication_classes=[authentication.BasicAuthentication]
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=OrderSerializer

    def list(self,request,*args,**kwargs):
        qs=CakeOrder.objects.filter(username=request.user)
        serializer=OrderSerializer(qs,many=True)
        return Response(data=serializer.data)
    

    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        instance=CakeOrder.objects.get(id=id)
        if instance.username==request.user:
            instance.delete()
            return Response(data={"msg":"deleted"})
        else:
            return Response(data={"msg":"permission denied"})



