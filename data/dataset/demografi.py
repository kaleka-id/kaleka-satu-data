from django.contrib import admin
from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from .alamat import Alamat
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin

class Demografi(models.Model):
  class Meta:
    verbose_name = 'Demografi'
    verbose_name_plural = 'Demografi'
    permissions = [
      ('search_demografi', 'Can search Demografi in Dictionary'),
    ]

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  alamat = models.ForeignKey(Alamat, on_delete=models.CASCADE)
  tahun = models.PositiveSmallIntegerField(validators=[MaxValueValidator(2100), MinValueValidator(1900)])
  penduduk_lakilaki = models.PositiveIntegerField()
  penduduk_perempuan = models.PositiveIntegerField()
  dasar_hukum = models.CharField(max_length=120)
  status_data = models.CharField(max_length=11, verbose_name='Status Data', choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')])
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

@admin.register(Demografi)
class DemografiModel(ImportExportModelAdmin):
  search_fields = ('alamat',)
  list_filter = ('alamat', 'tahun', 'dasar_hukum', 'status_data', 'created_at', 'updated_at', 'user')
  list_display = ('id', 'alamat', 'tahun', 'dasar_hukum', 'updated_at', 'user')
  readonly_fields = ('user',)
  raw_id_fields = ('alamat',)

  # Decrease pagination for performance in Django Admin
  list_per_page = 25

  def save_model(self, request, obj, form, change): 
    obj.user = request.user
    obj.save()