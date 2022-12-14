from django.db import models
import uuid
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.gis.admin import OSMGeoAdmin
from django.utils.crypto import get_random_string

def get_random_for_slug():
    return get_random_string(length=40)

# Create your models here.
class Shop(models.Model):
    class Meta:
        verbose_name = 'Testing - Shop'
        verbose_name_plural = 'Testing - Shop'

    name_shop = models.CharField(verbose_name='Shop Name', max_length=100)
    geom = models.PointField(verbose_name='Location', null=True, blank=True)
    address = models.CharField(max_length=100)
    Open = models.BooleanField(verbose_name='Is the shop is open?')
    capacity = models.IntegerField()
    slug = models.SlugField(max_length=40, unique=True, default=get_random_for_slug)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_shop

@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name_shop', 'geom', 'updated_at', 'user')


class Testing(models.Model):
    class Meta:
        verbose_name = 'Testing - Artikel'
        verbose_name_plural = 'Testing - Artikel'

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    kode = models.CharField(max_length=5)
    nama = models.CharField(max_length=30)
    deskripsi = models.TextField()
    slug = models.SlugField(max_length=40, unique=True, default=get_random_for_slug)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama

@admin.register(Testing)
class TestingModel(admin.ModelAdmin):
    search_fields = ('kode', 'nama')
    list_filter = ('kode', 'nama', 'created_at', 'updated_at', 'user')
    list_display = ('id', 'kode', 'nama', 'created_at', 'updated_at', 'user')
