from .models import House, User, Dates
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields =('id','email','username','password','first_name','last_name','phone')

class houseSerializers(serializers.ModelSerializer):
    class Meta:
        model = House
        fields ='__all__'



class datesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dates
        fields ='__all__'
