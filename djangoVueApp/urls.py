from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('overview/', views.apiOverview, name="api_overview"),
    path('houses-list/', views.housesList.as_view(), name="houses_list"),
    path('houses-list/<str:uid>/', views.userHouses, name="houses_list"),
    path('house-create/', views.houseCreate, name="house_create"),
    path('house-update/<str:pk>/', views.houseUpdate.as_view(), name="house_update"),
    path('house-details/<str:pk>/', views.houseDetails, name="house_detail"),
    path('house-delete/<str:pk>/', views.houseDelete.as_view(), name="house_delete"),
    path('dates/', views.dates.as_view(), name="dates_create"),
    path('dates-update/<str:pk>/', views.datesUpdate.as_view(), name="dates_update"),
    path('dates-delete/<str:pk>/', views.datesDelete.as_view(), name="dates_delete"),
    path('dates-house/<str:hid>/', views.datesHouse, name="dates_house"),
]   

