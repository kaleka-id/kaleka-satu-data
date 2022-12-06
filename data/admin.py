from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop

# Register your models here.
@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location', 'updated_at', 'user')
