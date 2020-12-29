from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets,generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view,action
from .models import House,User,Dates
from .serializers import houseSerializers,datesSerializers, GoogleSocialAuthSerializer, TwitterAuthSerializer, FacebookSocialAuthSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from .filters import HouseFilter
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
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



  #social 
class GoogleSocialAuthView(GenericAPIView):

    serializer_class = GoogleSocialAuthSerializer

    def post(self, request):
        """

        POST with "auth_token"

        Send an idtoken as from google to get user information

        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['auth_token'])
        return Response(data, status=status.HTTP_200_OK)


class FacebookSocialAuthView(GenericAPIView):

    serializer_class = FacebookSocialAuthSerializer

    def post(self, request):
        """

        POST with "auth_token"

        Send an access token as from facebook to get user information

        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['auth_token'])
        return Response(data, status=status.HTTP_200_OK)
