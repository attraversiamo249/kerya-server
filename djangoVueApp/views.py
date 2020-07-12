from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import House,User
from .serializers import houseSerializers
from.forms import CreateUserForm
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
        api_urls={
                'Houses list':'/houses_list',    
                'House create':'/house_create',
                'House details':'/house_details/<str:pk>/',
        }
        return Response(api_urls)
        #list
@api_view(['GET'])
def housesList(request):
        houses = House.objects.all()
        serializer = houseSerializers(houses, many=True)
        return Response(serializer.data)



        #details
@api_view(['GET'])
def houseDetails(request, pk):
        house = House.objects.get(id=pk)
        serializer = houseSerializers(house, many=False)
        return Response(serializer.data)       


        #create
@api_view(['POST'])
def houseCreate(request):
        serializer = houseSerializers(data=request.data)
        if serializer.is_valid():
                serializer.save

        return Response("sayi creayinah")                      


        #delete
@api_view(['DELETE'])
def houseDelete(request,pk):
        house = House.objects.get(id=pk)
        house.delete()
        return Response("sayi m7inah") 



