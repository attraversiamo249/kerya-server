from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import House,User, pickeddatesClient


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields =('id','email','username','password','first_name','last_name','phone','age')

class houseSerializers(serializers.ModelSerializer):
    class Meta:
        model = House
        fields ='__all__'


class pickeddatesSerializers(serializers.ModelSerializer):
    class Meta:
        model = pickeddatesClient
        fields ='__all__'





