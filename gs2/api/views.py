import re
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User   
from .serilizers import UserSerializer
from rest_framework import status
# Create your views here.

@api_view(['POST','GET','DELETE','PUT','PATCH'])
def hello_world(request,pk=None):
     if request.method == "GET":
        id = pk           
        if id is not None:
            usr = User.objects.get(id=id)
            ser = UserSerializer(usr)
            return Response(ser.data)
        usr = User.objects.all()
        ser = UserSerializer(usr, many=True)
        return Response(ser.data)
     if request.method == 'POST': 
        ser = UserSerializer(data=request.data)
        if ser.is_valid(): 
           ser.save()
           return Response({'msg':'data Created'},status =status.HTTP_201_CREATED)
        return Response(ser.errors)
     if request.method == 'PUT':
        id = request.data.get('id')
        usr = User.objects.get(id=id)
        ser = UserSerializer(usr, data= request.data)
        if ser.is_valid():
           ser.save()
           return Response({"msg":"success"})
        return Response(ser.errors)
     if request.method == 'PATCH':
        id = pk
      #   id = request.data.get('id')
        usr = User.objects.get(id=id)
        ser = UserSerializer(usr, data= request.data,partial = True)
        if ser.is_valid():
           ser.save()
           return Response({"msg":"success"})
        return Response(ser.errors)
     if request.method == 'DELETE':
            id = pk
            usr = User.objects.get(pk=id)
            usr.delete()
            return Response({"msg":"data deleted"})
            
        