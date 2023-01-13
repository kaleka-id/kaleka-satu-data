from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from django.contrib.gis.db import models
import uuid
from data.dataset.orang import Orang
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class Lahan(models.Model):
  class Meta:
    verbose_name = 'Lahan'
    verbose_name_plural = 'Lahan'
    permissions = [
      ('search_lahan', 'Can search Lahan in Dictionary')
    ]

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  geom = models.PolygonField(verbose_name='Lahan')
  petani = models.ForeignKey(Orang, on_delete=models.CASCADE, help_text=mark_safe('Gunakan tabel <a target="blank" href="/dict/orang/">Orang</a> sebagai referensi untuk mengisi bagian ini'))
  status_petani = models.CharField(max_length=10, choices=[('pemilik', 'Pemilik Lahan'), ('penggarap', 'Penggarap Lahan')])
  jenis_legalitas = models.CharField(max_length=25, null=True, blank=True, choices=[('Hak Milik', 'Hak Milik'), ('Hak Sewa', 'Hak Sewa'), ('Hak Guna Lahan', 'Hak Guna Lahan'), ('Hak Guna Bangunan', 'Hak Guna Bangunan'), ('Girik', 'Girik'), ('Surat Keterangan Tanah', 'Surat Keterangan Tanah'), ('Tanah Adat', 'Tanah Adat'), ('Tanpa Status', 'Tidak ada Status (Komunal)')])
  nomor_legalitas = models.CharField(max_length=20)
  tahun_legalitas = models.PositiveSmallIntegerField(validators=[MaxValueValidator(2100), MinValueValidator(1900)])
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

@admin.register(Lahan)
class LahanModel(LeafletGeoAdmin):
  search_fields = ('petani', 'nomor_legalitas')
  list_filter = ('status_petani', 'jenis_legalitas', 'tahun_legalitas', 'created_at', 'updated_at', 'user')
  list_display = ('id', 'petani', 'jenis_legalitas', 'updated_at', 'user')
  raw_id_fields = ('petani',)
  readonly_fields = ('user',)

  # Decrease pagination for performance in Django Admin
  list_per_page = 25

  def save_model(self, request, obj, form, change): 
    obj.user = request.user
    obj.save()