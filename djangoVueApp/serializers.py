from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import House, User, Dates


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields =('id','email','username','password','first_name','last_name','phone')

class houseSerializers(serializers.ModelSerializer):
    class Meta:
        model = House
        fields ='__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields =('image1','image2','image3','image4','image5')



class datesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dates
        fields ='__all__'
