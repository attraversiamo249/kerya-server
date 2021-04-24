from django_filters import rest_framework as filters
from .models import House

class HouseFilter(filters.FilterSet):
    ChoicesType=(
        ("Appartement","Appartement"),
        ("Villa","Villa"),
        ("Studio","Studio"),
        ("Chambre colocation","Chambre colocation")

    )
    ChoicesRooms=(
        ("2","two"),
        ("3","three"),
        ("4","+four")
    )

    type = filters.MultipleChoiceFilter(field_name="type",lookup_expr="exact",required=False,choices=ChoicesType)
    price = filters.NumericRangeFilter(field_name="price")
    rooms = filters.MultipleChoiceFilter(field_name="rooms",lookup_expr="exact",required=False,choices=ChoicesRooms)
    rooms_gte= filters.NumberFilter(field_name="rooms",lookup_expr="gte",required=False)
    class Meta: 
        model = House
        fields = ['city','type','address','rooms','price_min','price_max','rooms_gte']