from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.conf.urls.static import static
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def test(request):
    return render(request, 'base.html')

urlpatterns = [
    path('', home, name='home'),
    path('test/', test, name='test')
]
