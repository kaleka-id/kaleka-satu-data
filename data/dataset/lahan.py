from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from django.contrib.gis.db import models
import uuid
from data.dataset.orang import Orang
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin

# 🚨DATASET POLIGON LAHAN🚨
class LahanPoligon(models.Model):
  class Meta:
    verbose_name = 'Poligon Lahan'
    verbose_name_plural = 'Poligon Lahan'
    permissions = [
      ('search_lahanpoligon', 'Can search Poligon Lahan in Dictionary')
    ]

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  geom = models.PolygonField(verbose_name='Lahan', null=True, blank=True)
  status_data = models.CharField(max_length=20, choices=[('Updated', 'Updated'), ('Need Confirmation', 'Need Confirmation'), ('Not Valid', 'Not Valid')], default='Need Confirmation')
  keterangan = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

@admin.register(LahanPoligon)
class LahanPoligonModel(LeafletGeoAdmin):
  list_filter = ('status_data', 'created_at', 'updated_at', 'user')
  list_display = ('id', 'status_data', 'updated_at', 'user')
  readonly_fields = ('user',)

  # Decrease pagination for performance in Django Admin
  list_per_page = 25

  def save_model(self, request, obj, form, change): 
    obj.user = request.user
    obj.save()

# 🚨DATASET LEGALITAS LAHAN🚨
class LahanLegalitas(models.Model):
  class Meta:
    verbose_name = 'Legalitas Lahan'
    verbose_name_plural = 'Legalitas Lahan'
    permissions = [
      ('search_lahanlegalitas', 'Can search Legalitas Lahan in Dictionary')
    ]

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  jenis_legalitas = models.CharField(max_length=25, null=True, blank=True, 
    choices=[
      ('Hak Milik', 'Hak Milik'), 
      ('Hak Sewa', 'Hak Sewa'), 
      ('Hak Guna Lahan', 'Hak Guna Lahan'), 
      ('Hak Guna Bangunan', 'Hak Guna Bangunan'), 
      ('Girik', 'Girik'), 
      ('Surat Keterangan Tanah', 'Surat Keterangan Tanah'), 
      ('Tanah Adat', 'Tanah Adat'), 
      ('Tanpa Status', 'Tidak ada Status (Komunal)')])
  nomor_legalitas = models.CharField(max_length=40)
  luas_pada_dokumen = models.DecimalField(max_digits=10, decimal_places=2, help_text='Satuan dalam Ha, jika satuannya lain mohon dikonversi terlebih dahulu')
  tahun_legalitas = models.PositiveSmallIntegerField(validators=[MaxValueValidator(2100), MinValueValidator(1900)])
  status_data = models.CharField(max_length=20, choices=[('Updated', 'Updated'), ('Need Confirmation', 'Need Confirmation'), ('Not Valid', 'Not Valid')], default='Need Confirmation')
  keterangan = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

@admin.register(LahanLegalitas)
class LahanLegalitasModel(ImportExportModelAdmin):
  search_fields = ('nomor_legalitas',)
  list_filter = ('jenis_legalitas', 'tahun_legalitas', 'status_data', 'created_at', 'updated_at', 'user')
  list_display = ('id', 'jenis_legalitas', 'nomor_legalitas', 'status_data', 'updated_at', 'user')
  readonly_fields = ('user',)

  # Decrease pagination for performance in Django Admin
  list_per_page = 25

  def save_model(self, request, obj, form, change): 
    obj.user = request.user
    obj.save()

# 🚨DATASET LEGALITAS LAHAN - DOKUMEN LINGKUNGAN🚨
class LahanLegalitasLingkungan(models.Model):
  class Meta:
    verbose_name = 'Legalitas Lahan - Dokumen Lingkungan '
    verbose_name_plural = 'Legalitas Lahan - Dokumen Lingkungan'
    permissions = [
      ('search_lahanlegalitaslingkungan', 'Can search Legalitas Lahan - Dokumen Lingkungan in Dictionary')
    ]

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  legalitas_lahan = models.ForeignKey(LahanLegalitas, on_delete=models.CASCADE)
  jenis_dokumen = models.CharField(max_length=20, null=True, blank=True, 
    choices=[
      ('SPPL', 'SPPL (Surat Pernyataan Pengelolaan Lingkungan)'),
      ('UKL-UPL', 'Upaya Pengelolaan Lingkungan dan Upaya Pemantauan Lingkungan Hidup (UKL-UPL)'),
      ('AMDAL', 'Analisis Mengenai Dampak Lingkungan (AMDAL)')])
  nomor_dokumen = models.CharField(max_length=60)
  tahun_dokumen = models.PositiveSmallIntegerField(validators=[MaxValueValidator(2100), MinValueValidator(1900)])
  status_dokumen = models.CharField(max_length=20, choices=[('Berlaku', 'Berlaku'), ('Tidak Berlaku', 'Tidak Berlaku')])
  status_data = models.CharField(max_length=20, choices=[('Updated', 'Updated'), ('Need Confirmation', 'Need Confirmation'), ('Not Valid', 'Not Valid')], default='Need Confirmation')
  keterangan = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

@admin.register(LahanLegalitasLingkungan)
class LahanLegalitasLingkunganModel(ImportExportModelAdmin):
  search_fields = ('nomor_dokumen',)
  list_filter = ('jenis_dokumen', 'tahun_dokumen', 'status_dokumen', 'status_data', 'created_at', 'updated_at', 'user')
  list_display = ('id', 'jenis_dokumen', 'nomor_dokumen', 'status_dokumen', 'status_data', 'updated_at', 'user')
  raw_id_fields = ('legalitas_lahan',)
  readonly_fields = ('user',)

  # Decrease pagination for performance in Django Admin
  list_per_page = 25

  def save_model(self, request, obj, form, change): 
    obj.user = request.user
    obj.save()

# 🚨DATASET LEGALITAS LAHAN - DOKUMEN STDB🚨
class LahanLegalitasSTDB(models.Model):
  class Meta:
    verbose_name = 'Legalitas Lahan - Dokumen STDB '
    verbose_name_plural = 'Legalitas Lahan - Dokumen STDB'
    permissions = [
      ('search_lahanlegalitasstdb', 'Can search Legalitas Lahan - Dokumen STDB in Dictionary')
    ]

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  legalitas_lahan = models.ForeignKey(LahanLegalitas, on_delete=models.CASCADE)
  nomor_dokumen = models.CharField(max_length=60)
  tahun_dokumen = models.PositiveSmallIntegerField(validators=[MaxValueValidator(2100), MinValueValidator(1900)])
  status_dokumen = models.CharField(max_length=20, choices=[('Berlaku', 'Berlaku'), ('Tidak Berlaku', 'Tidak Berlaku')])
  jumlah_pohon = models.IntegerField()
  tahun_tanam = models.PositiveSmallIntegerField(validators=[MaxValueValidator(2100), MinValueValidator(1900)])
  status_data = models.CharField(max_length=20, choices=[('Updated', 'Updated'), ('Need Confirmation', 'Need Confirmation'), ('Not Valid', 'Not Valid')], default='Need Confirmation')
  keterangan = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

@admin.register(LahanLegalitasSTDB)
class LahanLegalitasSTDBModel(ImportExportModelAdmin):
  search_fields = ('nomor_dokumen',)
  list_filter = ('tahun_dokumen', 'status_dokumen', 'jumlah_pohon', 'tahun_tanam', 'status_data', 'created_at', 'updated_at', 'user')
  list_display = ('id', 'nomor_dokumen', 'status_dokumen', 'jumlah_pohon', 'tahun_tanam', 'status_data', 'updated_at', 'user')
  raw_id_fields = ('legalitas_lahan',)
  readonly_fields = ('user',)

  # Decrease pagination for performance in Django Admin
  list_per_page = 25

  def save_model(self, request, obj, form, change): 
    obj.user = request.user
    obj.save()

# 🚨DATASET LAHAN🚨
class Lahan(models.Model):
  class Meta:
    verbose_name = 'Lahan'
    verbose_name_plural = 'Lahan'
    permissions = [
      ('search_lahan', 'Can search Lahan in Dictionary')
    ]

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  poligon_lahan = models.OneToOneField(LahanPoligon, on_delete=models.CASCADE, null=True, blank=True, help_text=mark_safe('Gunakan tabel <a target="blank" href="/dict/lahan/poligon">Poligon Lahan</a> sebagai referensi untuk mengisi bagian ini'))
  petani = models.ForeignKey(Orang, on_delete=models.CASCADE, null=True, blank=True, help_text=mark_safe('Gunakan tabel <a target="blank" href="/dict/orang/">Orang</a> sebagai referensi untuk mengisi bagian ini'))
  status_petani = models.CharField(max_length=10, choices=[('pemilik', 'Pemilik Lahan'), ('penggarap', 'Penggarap Lahan')], null=True, blank=True)
  legalitas = models.OneToOneField(LahanLegalitas, on_delete=models.CASCADE, null=True, blank=True, help_text=mark_safe('Gunakan tabel <a target="blank" href="/dict/lahan/legalitas/">Legalitas Lahan</a> sebagai referensi untuk mengisi bagian ini'))
  status_data = models.CharField(max_length=20, choices=[('Updated', 'Updated'), ('Need Confirmation', 'Need Confirmation'), ('Not Valid', 'Not Valid')], default='Need Confirmation')
  keterangan = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

@admin.register(Lahan)
class LahanModel(ImportExportModelAdmin):
  search_fields = ('petani__nama_lengkap',)
  list_filter = ('status_petani', 'status_data', 'created_at', 'updated_at', 'user')
  list_display = ('id', 'petani', 'status_data', 'updated_at', 'user')
  raw_id_fields = ('poligon_lahan', 'petani', 'legalitas')
  readonly_fields = ('user',)

  # Decrease pagination for performance in Django Admin
  list_per_page = 25

  def save_model(self, request, obj, form, change): 
    obj.user = request.user
    obj.save()