from django_filters import rest_framework as filters
from .models import House

class HouseFilter(filters.FilterSet):
    type = filters.TypedMultipleChoiceFilter(field_name="type",lookup_expr="exact")
    max_price = filters.NumberFilter(field_name="price",lookup_expr="lte")
    rooms = filters.TypedMultipleChoiceFilter(field_name="type",lookup_expr="exact")

    class Meta: 
        model = House
        fields = ['city','type','address','rooms','max_price']