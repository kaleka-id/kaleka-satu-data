from django.urls import path, include

# PAGE VIEW AND FORM
from .pages.menu import *

urlpatterns = [
    path('', home, name='home'),
    path('forms/', forms, name='forms'),

    # EXTENSION PATH
    path('', include('operation.ext_urls.testing')),
]
