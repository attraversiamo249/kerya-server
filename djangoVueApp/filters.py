from django_filters import rest_framework as filters
from .models import House

class HouseFilter(filters.FilterSet):
    ChoicesType=(
        ("app","Appartement"),
        ("villa","Villa")
    )
    ChoicesRooms=(
        ("app","Appartement"),
        ("villa","Villa")
    )

    type = filters.MultipleChoiceFilter(field_name="type",lookup_expr="exact",required=False,choices=ChoicesType)
    max_price = filters.NumberFilter(field_name="price",lookup_expr="lte",required=False)
    rooms = filters.MultipleChoiceFilter(field_name="type",lookup_expr="exact",required=False,choices=ChoicesRooms)

    class Meta: 
        model = House
        fields = ['city','type','address','rooms','max_price']