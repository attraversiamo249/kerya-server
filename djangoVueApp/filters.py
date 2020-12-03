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
    max_price = filters.NumberFilter(field_name="price",lookup_expr="lte",required=False)
    rooms = filters.MultipleChoiceFilter(field_name="rooms",lookup_expr="exact",required=False,choices=ChoicesRooms)
    rooms_gte= filters.NumberFilter(field_name="rooms",lookup_expr="gte",required=False)
    class Meta: 
        model = House
        fields = ['city','type','address','rooms','max_price','rooms_gte']