from django.contrib import admin
from django.contrib.gis.db import models
import uuid
from .alamat import Alamat
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin

class WilayahDesa(models.Model):
  class Meta:
    verbose_name = 'Wilayah Desa'
    verbose_name_plural = 'Wilayah Desa'
    permissions = [
      ('search_wilayahdesa', 'Can search Wilayah Desa in Dictionary'),
    ]

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  geom = models.MultiPolygonField(verbose_name='Lokasi', db_index=True)
  source_id = models.CharField(max_length=50)
  catatan = models.CharField(max_length=100, null=True, blank=True)
  alamat_1 = models.ForeignKey(Alamat, related_name='alamat', on_delete=models.CASCADE, null=True, blank=True)
  alamat_2 = models.ForeignKey(Alamat, related_name='alamat_2', on_delete=models.CASCADE, null=True, blank=True)
  alamat_3 = models.ForeignKey(Alamat, related_name='alamat_3', on_delete=models.CASCADE, null=True, blank=True)
  alamat_4 = models.ForeignKey(Alamat, related_name='alamat_4', on_delete=models.CASCADE, null=True, blank=True)
  srs = models.CharField(max_length=30)
  metadata = models.TextField(null=True, blank=True)
  status_data = models.CharField(max_length=11, verbose_name='Status Data', choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')])
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

@admin.register(WilayahDesa)
class WilayahDesaModel(ImportExportModelAdmin):
  # search_fields = ('alamat',)
  list_filter = ('alamat_1', 'alamat_2', 'alamat_3', 'alamat_4', 'status_data', 'created_at', 'updated_at', 'user')
  list_display = ('id', 'source_id', 'updated_at', 'user')
  raw_id_fields = ('alamat_1', 'alamat_2', 'alamat_3', 'alamat_4')

  # Decrease pagination for performance in Django Admin
  list_per_page = 25

  def save_model(self, request, obj, form, change): 
    obj.user = request.user
    obj.save()