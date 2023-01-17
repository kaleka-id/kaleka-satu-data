from django.urls import path, include

# PAGE VIEW AND FORM
from .pages.menu import *

urlpatterns = [
    path('', include('operation.pages.alamat')),
    path('', include('operation.pages.kbji')),
    path('', include('operation.pages.kegiatan')),
    path('', include('operation.pages.lahan')),
    path('', include('operation.pages.menu')),
    path('', include('operation.pages.orang')),
    path('', include('operation.pages.profesi')),
    path('', include('operation.pages.testing')),
]


