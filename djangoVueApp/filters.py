from django_filters import rest_framework as filters
from .models import House

class HouseFilter(filters.FilterSet):
    min_rooms = filters.NumberFilter(field_name="rooms", lookup_expr='gte')
    max_rooms = filters.NumberFilter(field_name="rooms", lookup_expr='lte')
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta: 
        model = House
        fields = ['city','type','address','min_rooms','min_rooms','min_price','max_price']