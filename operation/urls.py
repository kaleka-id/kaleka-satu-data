from django.urls import path, include

# PAGE VIEW AND FORM
from .pages.menu import *

urlpatterns = [
    path('', include('operation.pages.menu')),
    path('', include('operation.pages.testing')),
]


