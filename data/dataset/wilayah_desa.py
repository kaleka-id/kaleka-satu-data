from django.contrib import admin
from django.contrib.gis.db import models
import uuid
from .alamat import Alamat
from django.contrib.auth.models import User

class WilayahDesa(models.Model):
  class Meta:
    verbose_name = 'Wilayah Desa'
    verbose_name_plural = 'Wilayah Desa'
    permissions = [
      ('search_wilayahdesa', 'Can search Wilayah Desa in Dictionary'),
    ]

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  alamat = models.ForeignKey(Alamat, on_delete=models.CASCADE)
  geom = models.MultiPolygonField(verbose_name='Lokasi', db_index=True)
  dasar_hukum = models.CharField(max_length=120)
  status_data = models.CharField(max_length=11, verbose_name='Status Data', choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')])
  keterangan = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

@admin.register(WilayahDesa)
class WilayahDesaModel(admin.ModelAdmin):
  search_fields = ('alamat',)
  list_filter = ('alamat', 'status_data', 'created_at', 'updated_at', 'user')
  list_display = ('id', 'alamat', 'updated_at', 'user')
  raw_id_fields = ('alamat',)

  # Decrease pagination for performance in Django Admin
  list_per_page = 25

  def save_model(self, request, obj, form, change): 
    obj.user = request.user
    obj.save()