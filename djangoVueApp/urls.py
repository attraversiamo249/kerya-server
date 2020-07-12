from django.urls import path, include
from . import views



urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('overview/', views.apiOverview, name="api_overview"),
    path('houses-list/', views.housesList, name="houses_list"),
    path('house-create/', views.houseCreate, name="house_create"),
    path('house-details/<str:pk>/', views.houseDetails, name="house_detail"),
    path('house-delete/<str:pk>/', views.houseDelete, name="house_Delete"),
]