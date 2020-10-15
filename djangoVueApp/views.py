from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets,generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view,action
from .models import House,User,Dates
from .serializers import houseSerializers,datesSerializers
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from .filters import HouseFilter
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FileSerializer
# Create your views here.

@action(detail=True, methods=['patch'])
class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = FileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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