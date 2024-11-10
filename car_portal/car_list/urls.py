from django.urls import path
from .views import car_list

urlpatterns = [
    path('car-list/', car_list, name = "Car_list"),
]