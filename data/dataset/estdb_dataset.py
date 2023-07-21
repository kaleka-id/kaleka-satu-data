from django.contrib import admin
from django.contrib.gis.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator, MaxLengthValidator, MinLengthValidator
from django.contrib.auth.models import User
import uuid
from import_export.admin import ImportExportModelAdmin

class PetaniSTDB(models.Model):
  class Meta:
    verbose_name = '[TEMPORARY] Petani STDB'
    verbose_name_plural = '[TEMPORARY] Petani STDB'
    permissions = [
      ('search_petani_stdb', 'Can search petani STDB in Dictionary'),
    ]

  id = models.UUIDField(default=uuid.uuid4, db_index=True, editable=False, primary_key=True)
  nik = models.CharField(max_length=16, null=True, blank=True)
  nama = models.CharField(max_length=100, null=True, blank=True)
  tempat_lahir = models.CharField(max_length=50, null= True, blank=True)
  tanggal_lahir = models.DateField(null=True, blank=True)
  nkk = models.CharField(max_length=16, null=True, blank=True)
  email = models.EmailField(null=True, blank=True)
  no_telepon = models.CharField(max_length=20, null=True, blank=True, validators=[RegexValidator(regex='\d+', message='Input must a valid number', code='invalid number')])
  keanggotaan_organisasi = models.CharField(max_length=25, null=True, blank=True)
  keanggotaan_organisasi_id = models.CharField(max_length=25, null=True, blank=True)
  keanggotaan_organisasi_lainnya = models.CharField(max_length=50, null=True, blank=True)
  nama_organisasi = models.CharField(max_length=100, null=True, blank=True)
  sumber_data = models.CharField(max_length=20, null=True, blank=True)
  sumber_data_id = models.CharField(max_length=20, null=True, blank=True)
  sumber_data_lainnya = models.CharField(max_length=100, null=True, blank=True)
  kode_provinsi = models.SmallIntegerField(null=True, blank=True, validators=[MinLengthValidator(2), MaxLengthValidator(2)])
  kode_kabupaten = models.IntegerField(null=True, blank=True, validators=[MinLengthValidator(4), MaxLengthValidator(4)])
  kode_kecamatan = models.IntegerField(null=True, blank=True, validators=[MinLengthValidator(6), MaxLengthValidator(6)])
  kode_desa = models.BigIntegerField(null=True, blank=True, validators=[MinLengthValidator(10), MaxLengthValidator(10)])
  no_rt = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxLengthValidator(100)])
  no_rw = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxLengthValidator(100)])
  alamat_lengkap = models.TextField(null=True, blank=True)
  validasi_data = models.BooleanField(default=False)
  last_edited = models.DateTimeField(auto_now=True)
  user_last_edit = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)

@admin.register(PetaniSTDB)
class PetaniSTDBAdmin(ImportExportModelAdmin):
  search_fields = ('nama', 'nik')
  list_filter = ('kode_provinsi', 'kode_kabupaten', 'kode_kecamatan', 'kode_desa', 'last_edited', 'user_last_edit')
  list_display = ('id', 'nama', 'nik', 'last_edited', 'user_last_edit')
  readonly_fields = ('user_last_edit',)

  # Decrease pagination for performance in Django Admin
  list_per_page = 25

  def save_model(self, request, obj, form, change): 
    obj.user_last_edit = request.user
    obj.save()

class LahanSTDB(models.Model):
  class Meta:
    verbose_name = '[TEMPORARY] Lahan STDB'
    verbose_name_plural = '[TEMPORARY] Lahan STDB'
    permissions = [
      ('search_lahan_stdb', 'Can search Lahan STDB in Dictionary'),
    ]
  
  id = models.UUIDField(default=uuid.uuid4, db_index=True, editable=False, primary_key=True)
  petani_id = models.ForeignKey(PetaniSTDB, db_index=True, null=True, blank=True, on_delete=models.SET_NULL)
  status_kepemilikan_lahan = models.CharField(max_length=30, null=True, blank=True)
  status_kepemilikan_lahan_id = models.CharField(max_length=30, null=True, blank=True)
  status_kepemilikan_lahan_lainnya = models.CharField(max_length=50, null=True, blank=True)
  nomor_registrasi_kepemilikan = models.CharField(max_length=100, null=True, blank=True)
  luas_polygon_ha = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
  luas_bukti_kepemilikan_ha = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
  komoditas = models.CharField(max_length=50, null=True, blank=True)
  komoditas_id = models.CharField(max_length=50, null=True, blank=True)
  produksi_tahunan = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
  tempat_jual = models.CharField(max_length=30, null=True, blank=True)
  tempat_jual_id = models.CharField(max_length=30, null=True, blank=True)
  nama_pembeli = models.CharField(max_length=50, null=True, blank=True)
  tahun_tanam = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1900), MaxValueValidator(2100)])
  jumlah_pohon = models.PositiveIntegerField(null=True, blank=True)
  pola_tanam = models.CharField(max_length=30, null=True, blank=True)
  pola_tanam_id = models.CharField(max_length=30, null=True, blank=True)
  jenis_lahan = models.CharField(max_length=30, null=True, blank=True)
  jenis_lahan_id = models.CharField(max_length=30, null=True, blank=True)
  asal_benih = models.CharField(max_length=50, null=True, blank=True)
  asal_benih_id = models.CharField(max_length=50, null=True, blank=True)
  asal_benih_lainnya = models.CharField(max_length=50, null=True, blank=True)
  jenis_pupuk = models.CharField(max_length=50, null=True, blank=True)
  jenis_pupuk_id = models.CharField(max_length=50, null=True, blank=True)
  mitra_pengolahan = models.CharField(max_length=50, null=True, blank=True)
  mitra_pengolahan_id = models.CharField(max_length=50, null=True, blank=True)
  mitra_pengolahan_lainnya = models.CharField(max_length=50, null=True, blank=True)
  usaha_lain_kebun = models.CharField(max_length=50, null=True, blank=True)
  geom = models.PolygonField(db_index=True, null=True, blank=True)
  kode_provinsi = models.SmallIntegerField(null=True, blank=True, validators=[MinLengthValidator(2), MaxLengthValidator(2)])
  kode_kabupaten = models.IntegerField(null=True, blank=True, validators=[MinLengthValidator(4), MaxLengthValidator(4)])
  kode_kecamatan = models.IntegerField(null=True, blank=True, validators=[MinLengthValidator(6), MaxLengthValidator(6)])
  kode_desa = models.BigIntegerField(null=True, blank=True, validators=[MinLengthValidator(10), MaxLengthValidator(10)])
  no_rt = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxLengthValidator(100)])
  no_rw = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxLengthValidator(100)])
  alamat_lengkap = models.TextField(null=True, blank=True)
  validasi_data = models.BooleanField(default=False)
  last_edited = models.DateTimeField(auto_now=True)
  user_last_edit = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)

@admin.register(LahanSTDB)
class LahanSTDBAdmin(ImportExportModelAdmin):
  search_fields = ('status_kepemilikan_lahan',)
  list_filter = ('kode_provinsi', 'kode_kabupaten', 'kode_kecamatan', 'kode_desa', 'last_edited', 'user_last_edit')
  list_display = ('id', 'geom', 'status_kepemilikan_lahan', 'last_edited', 'user_last_edit')
  readonly_fields = ('user_last_edit',)

  # Decrease pagination for performance in Django Admin
  list_per_page = 25

  def save_model(self, request, obj, form, change): 
    obj.user_last_edit = request.user
    obj.save()