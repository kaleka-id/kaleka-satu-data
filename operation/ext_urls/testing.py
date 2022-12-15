from django.urls import path

# PAGE VIEW AND FORM
from ..pages.testing import *

urlpatterns = [
    path('dataset/testing-artikel/', testingArtikel, name='testing_artikel_list'),
    path('dataset/testing-artikel/<slug:slug>/', testingArtikelDetail, name='testing_artikel_detail'),
    path('dataset/testing-artikel-add/', article_form, name='testing_artikel_form'),
]
