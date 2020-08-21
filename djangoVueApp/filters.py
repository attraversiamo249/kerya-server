from django_filters import rest_framework as filters
from .models import House

class HouseFilter(filters.FilterSet):
    min_rooms = filters.NumberFilter(field_name="rooms", lookup_expr='gte')
    max_rooms = filters.NumberFilter(field_name="rooms", lookup_expr='lte')

    class Meta: 
        model = House
        fields = ['city','type','address','min_rooms','min_rooms','price']