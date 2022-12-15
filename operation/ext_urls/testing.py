from django.urls import path

# PAGE VIEW AND FORM
from ..pages.testing import *

urlpatterns = [
    path('dataset/testing-artikel/', testingArtikel, name='testing_artikel_list'),
    path('dataset/testing-artikel/<slug:slug>/', testingArtikelDetail, name='testing_artikel_detail'),
    path('dataset/testing-artikel-add/', article_form_add, name='testing_artikel_form'),
    path('dataset/testing-artikel-update/<slug:slug>/', article_form_update, name='testing_artikel_form_update'),
    path('dataset/testing-artikel-delete/<slug:slug>/', article_form_delete, name='testing_artikel_form_delete'),
]
