from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from .views import *


def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
