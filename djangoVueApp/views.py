from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets,generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import House,User,Dates
from .serializers import houseSerializers,datesSerializers
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from .filters import HouseFilter
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
        api_urls={
                'Houses list':'/houses_list',    
                'House create':'/house_create',
                'House details':'/house_details/<str:pk>/',
                'House update':'/house_update/<str:pk>/' 
        }
        return Response(api_urls)
        #list
class housesList(generics.ListAPIView):
        queryset = House.objects.all()  
        serializer_class = houseSerializers     
        pagination_class = PageNumberPagination
        filter_backends = (filters.DjangoFilterBackend,)
        filterset_class = HouseFilter
        
        

         #user_houses
@api_view(['GET'])      
def userHouses(request, uid):
        houses = House.objects.filter(user=uid)
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
                serializer.save()

        return Response(serializer.data)  
                            
   #update
@api_view(['POST'])
def houseUpdate(request,pk):
        house = House.objects.get(id=pk)
        serializer = houseSerializers(instance=house,data=request.data)
        if serializer.is_valid():
                serializer.save()

        return Response(serializer.data)  

        #delete
@api_view(['DELETE'])
def houseDelete(request,pk):
        house = House.objects.get(id=pk)
        house.delete()
        return Response("sayi m7inah") 

class datesList(generics.ListAPIView):
        queryset = Dates.objects.all()  
        serializer_class = datesSerializers   

@api_view(['POST'])
def addDates(request):
        serializer = datesSerializers(data=request.data)
        if serializer.is_valid():
                serializer.save()

        return Response(serializer.data)  

