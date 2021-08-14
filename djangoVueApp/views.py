from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets,generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view,action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django_filters import rest_framework as filters
from .models import House, User, Dates
from .serializers import houseSerializers,datesSerializers
from .filters import HouseFilter

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
        api_urls={
                'users':'kerya.herokuapp.com/api/users',    
                'houses list':'kerya.herokuapp.com/api/houses-list',    
                'House create':'kerya.herokuapp.com/api/house-create',
                'House details':'kerya.herokuapp.com/api/house-details',
                'House update':'kerya.herokuapp.com/api/houses-update',
                'dates create':'kerya.herokuapp.com/api/dates',
                'dates house':'kerya.herokuapp.com/api/dates-house'
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
class houseUpdate(generics.UpdateAPIView):
        queryset = House.objects.all()  
        serializer_class = houseSerializers     

        #delete
class houseDelete(generics.DestroyAPIView):
        queryset = House.objects.all()  
        serializer_class = houseSerializers     

            #dates
class dates(generics.ListCreateAPIView):
        queryset = Dates.objects.all()  
        serializer_class = datesSerializers     

class datesUpdate(generics.UpdateAPIView):
        queryset = Dates.objects.all()  
        serializer_class = datesSerializers   

class datesDelete(generics.DestroyAPIView):
        queryset = Dates.objects.all()  
        serializer_class = datesSerializers       


         #user_houses
@api_view(['GET'])      
def datesHouse(request, hid):
        dates = Dates.objects.filter(house=hid)
        serializer = datesSerializers(dates, many=True)
        return Response(serializer.data)



