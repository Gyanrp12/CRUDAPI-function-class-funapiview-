import json
from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import generics
from  django.utils.decorators import method_decorator
from django.views import View



@method_decorator(csrf_exempt, name = "dispatch")
class UserAPI(View):
    def get(self, request, *args, **kwargs): 
        json_data = request.body
        st = io.BytesIO(json_data)
        pydata = JSONParser().parse(st)
        id = pydata.get('id', None)
        if id is not None:
            usr = User.objects.get(id=id)
            ser = UserSerializer(usr)
            json_data = JSONRenderer().render(ser.data)
            return HttpResponse(json_data, content_type='application/json')
        
        usr = User.objects.all()
        ser = UserSerializer(usr, many=True)
        json_data = JSONRenderer().render(ser.data)
        return HttpResponse(json_data, content_type='application/json')
    
    def post(self, request, *args, **kwargs): 
        json_data = request.body 
        s = io.BytesIO(json_data)
        pydata = JSONParser().parse(s)
        ser = UserSerializer(data=pydata) #data is a syntax 
        if ser.is_valid():
            ser.save()
            msg ='data created'    
            j_data = JSONRenderer().render(msg)
            return HttpResponse(j_data,content_type='application/json')
        JSONRenderer().render(ser.errors) # this syntax show error in serlization if you have.
        return HttpResponse(j_data,content_type='application/json')
    def put(self, request, *args, **kwargs): 
        json_data = request.body
        st = io.BytesIO(json_data)
        pydata = JSONParser().parse(st)
        id = pydata.get('id')
        usr = User.objects.get(id=id)
        ser = UserSerializer(usr,data=pydata , partial=True)
        if ser.is_valid():
            ser.save()
            msg = 'updated'
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
    
    def DELETE(self, request, *args, **kwargs): 
        json_data = request.body
        st = io.BytesIO(json_data)
        pydata = JSONParser().parse(st)
        id = pydata.get('id')
        usr = User.objects.get(id=id)
        usr.delete()
        msg = "deleted"
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type='application/json')
    

# def user(request):
#     usr = User.objects.all()
#     serializer = UserSerializer(usr,many=True)
#     # json_data = JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data,content_type='application/json')
#     # return JsonResponse(serializer.data,safe=False)  

# @csrf_exempt
# def rest_api(request):
#     if request.method == "GET":
#         json_data = request.body
#         st = io.BytesIO(json_data)
#         pydata = JSONParser().parse(st)
#         id = pydata.get('id', None)
#         if id is not None:
#             usr = User.objects.get(id=id)
#             ser = UserSerializer(usr)
#             json_data = JSONRenderer().render(ser.data)
#             return HttpResponse(json_data, content_type='application/json')
        
#         usr = User.objects.all()
#         ser = UserSerializer(usr, many=True)
#         json_data = JSONRenderer().render(ser.data)
#         return HttpResponse(json_data, content_type='application/json')
#     if request.method == 'POST':
#         json_data = request.body 
#         s = io.BytesIO(json_data)
#         pydata = JSONParser().parse(s)
#         ser = UserSerializer(data=pydata) #data is a syntax 
#         if ser.is_valid():
#             ser.save()
#             msg ='data created'    
#             j_data = JSONRenderer().render(msg)
#             return HttpResponse(j_data,content_type='application/json')
#         JSONRenderer().render(ser.errors) # this syntax show error in serlization if you have.
#         return HttpResponse(j_data,content_type='application/json')
    
#     if request.method == 'PUT':
#         json_data = request.body
#         st = io.BytesIO(json_data)
#         pydata = JSONParser().parse(st)
#         id = pydata.get('id')
#         usr = User.objects.get(id=id)
#         ser = UserSerializer(usr,data=pydata , partial=True)
#         if ser.is_valid():
#             ser.save()
#             msg = 'updated'
#             json_data = JSONRenderer().render(msg)
#             return HttpResponse(json_data, content_type='application/json')
            
#     if request.method == 'DELETE':
#         json_data = request.body
#         st = io.BytesIO(json_data)
#         pydata = JSONParser().parse(st)
#         id = pydata.get('id')
#         usr = User.objects.get(id=id)
#         usr.delete()
#         msg = "deleted"
#         json_data = JSONRenderer().render(msg)
#         return HttpResponse(json_data, content_type='application/json')

# # class Usrist(generics.ListCreateAPIView):
# #     queryset = User.objects.all()
# #     ser_cls =  Userserializer
    
# # class Userdetail(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = User
# #     ser_cls = Userserializer
    