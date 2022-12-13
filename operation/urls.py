from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.conf.urls.static import static
from django.conf import settings

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('', home, name='home'),
]
