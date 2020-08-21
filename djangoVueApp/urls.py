from django.urls import path, include
from . import views



urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('overview/', views.apiOverview, name="api_overview"),
    path('houses-list/', views.housesList.as_view(), name="houses_list"),
    path('houses-list/<str:uid>/', views.userHouses, name="houses_list"),
    path('house-create/', views.houseCreate, name="house_create"),
    path('house-update/<str:pk>/', views.houseUpdate, name="house_update"),
    path('house-details/<str:pk>/', views.houseDetails, name="house_detail"),
    path('house-delete/<str:pk>/', views.houseDelete, name="house_Delete"),
    path('dates-list/', views.datesList.as_view(), name="dates-list"),
    path('dates-house/', views.addDates, name="dates-house"),

]