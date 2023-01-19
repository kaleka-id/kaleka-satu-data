from django.db import models
import uuid
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from data.validators import file_image
from django.utils.safestring import mark_safe
# from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin
from django_better_admin_arrayfield.models.fields import ArrayField
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from import_export.admin import ImportExportModelAdmin


# 🚨TOKO🚨
class Shop(models.Model):
    class Meta:
        verbose_name = 'Testing - Toko'
        verbose_name_plural = 'Testing - Toko'

    name_shop = models.CharField(verbose_name='Shop Name', max_length=100)
    geom = models.PointField(verbose_name='Location', null=True, blank=True)
    address = models.CharField(max_length=100)
    Open = models.BooleanField(verbose_name='Is the shop is open?')
    capacity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_shop

@admin.register(Shop)
class ShopAdmin(LeafletGeoAdmin):
    list_display = ('name_shop', 'geom', 'updated_at', 'user')


# 🚨ARTIKEL🚨
class Testing(models.Model):
    class Meta:
        verbose_name = 'Testing - Artikel'
        verbose_name_plural = 'Testing - Artikel'

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    kode = models.CharField(max_length=5)
    nama = models.CharField(max_length=30)
    deskripsi = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama

@admin.register(Testing)
class TestingModel(ImportExportModelAdmin):
    search_fields = ('kode', 'nama')
    list_filter = ('kode', 'nama', 'created_at', 'updated_at', 'user')
    list_display = ('id', 'kode', 'nama', 'created_at', 'updated_at', 'user')


# 🚨PRODUK🚨
class Product(models.Model):
    class Meta:
        verbose_name = 'Testing - Produk'
        verbose_name_plural = 'Testing - Produk'

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    nama = models.CharField(max_length=30)
    deskripsi = models.ForeignKey(Testing, on_delete=models.CASCADE, help_text=mark_safe('Gunakan tabel <a target="blank" href="/dict/testing-artikel/">Testing Artikel</a> sebagai referensi untuk mengisi bagian ini'))
    toko = models.ManyToManyField(Shop, blank=True)
    foto = models.FileField(upload_to='testing/', validators=[file_image], blank=True, null=True, help_text='Gunakan file ekstensi .jpg, .jpeg atau .png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama

@admin.register(Product)
class ProductModel(ImportExportModelAdmin, DynamicArrayMixin):
    search_fields = ('nama',)
    list_filter = ('nama', 'created_at', 'updated_at', 'user')
    list_display = ('id', 'nama', 'updated_at', 'user')
    filter_horizontal = ('toko',)
    raw_id_fields = ('deskripsi',)