from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

# PAGE VIEW AND FORM
from .pages.testing import *
from .pages.home import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password-change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('dataset/testing-artikel/', testingArtikel, name='testing_artikel_list'),
    path('dataset/testing-artikel/<slug:slug>/', testingArtikelDetail, name='testing_artikel_detail'),
    path('dataset/testing-artikel-add/', article_form, name='testing_artikel_form'),
]
