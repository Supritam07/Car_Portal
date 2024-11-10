from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def car_list(request):
    return HttpResponse("No cars to Show")