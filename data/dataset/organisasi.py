from django.contrib import admin
from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from .orang import Orang
from .alamat import Alamat
from import_export.admin import ImportExportModelAdmin

class Organisasi(models.Model):
  class Meta:
    verbose_name = 'Organisasi'
    verbose_name_plural = 'Organisasi'
    permissions = [
      ('search_organisasi', 'Can search Organisasi in Dictionary')
    ]

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  alamat = models.ForeignKey(Alamat, on_delete=models.CASCADE)
  status_data = models.CharField(max_length=20, choices=[('Updated', 'Updated'), ('Need Confirmation', 'Need Confirmation'), ('Not Valid', 'Not Valid')])
  keterangan = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

@admin.register(Organisasi)
class OrganisasiModel(ImportExportModelAdmin):
  list_display = ('id', 'status_data', 'updated_at', 'user')
  raw_id_fields = ('alamat',)
  readonly_fields = ('user',)

  # Decrease pagination for performance in Django Admin
  list_per_page = 25

  def save_model(self, request, obj, form, change): 
    obj.user = request.user
    obj.save()

class NamaOrganisasi(models.Model):
  class Meta:
    verbose_name = 'Nama Organisasi'
    verbose_name_plural = 'Nama Organisasi'

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  organisasi = models.ForeignKey(Organisasi, on_delete=models.CASCADE)
  nama_organisasi = models.CharField(max_length=80)
  status_organisasi = models.CharField(max_length=20, choices=[('Badan Hukum', 'Badan Hukum'), ('Non Badan Hukum', 'Non Badan Hukum'), ('Tidak diketahui', 'Tidak diketahui')])
  nama_notaris = models.CharField(max_length=50, null=True, blank=True)
  nomor_notaris = models.CharField(max_length=30, null=True, blank=True)
  tanggal_notaris = models.DateField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def save(self, *args, **kwargs):
    if self.nama_notaris != None: 
      self.nama_notaris = self.nama_notaris.upper()
    return super(NamaOrganisasi, self).save(*args, **kwargs)
  
  def __str__(self):
    return self.nama_organisasi

@admin.register(NamaOrganisasi)
class NamaOrganisasiModel(ImportExportModelAdmin):
  list_display = ('id', 'nama_organisasi', 'status_organisasi', 'nomor_notaris', 'updated_at', 'user')
  raw_id_fields = ('organisasi',)
  readonly_fields = ('user',)

  # Decrease pagination for performance in Django Admin
  list_per_page = 25

  def save_model(self, request, obj, form, change): 
    obj.user = request.user
    obj.save()

class PosisiOrganisasi(models.Model):
  class Meta:
    verbose_name = 'Posisi Organisasi'
    verbose_name_plural = 'Posisi Organisasi'

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  nama_posisi = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.nama_organisasi
  
@admin.register(PosisiOrganisasi)
class PosisiOrganisasiModel(ImportExportModelAdmin):
  list_display = ('id', 'nama_posisi', 'updated_at', 'user')
  readonly_fields = ('user',)

class KeanggotaanOrganisasi(models.Model):
  class Meta:
    verbose_name = 'Keanggotaan Organisasi'
    verbose_name_plural = 'Keanggotaan Organisasi'

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  organisasi = models.ForeignKey(Organisasi, on_delete=models.CASCADE)
  orang = models.ForeignKey(Orang, on_delete=models.CASCADE)
  posisi = models.ForeignKey(PosisiOrganisasi, on_delete=models.CASCADE)
  bergabung_sejak = models.DateField(default='1900-01-01')
  status = models.CharField(max_length=50, choices=[('Aktif', 'Aktif'), ('Non Aktif', 'Non Aktif')])
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

@admin.register(KeanggotaanOrganisasi)
class KeanggotaanOrganisasiModel(ImportExportModelAdmin):
  list_display = ('id', 'orang', 'posisi', 'bergabung_sejak', 'updated_at', 'user')
  raw_id_fields = ('organisasi', 'orang', 'posisi')
  readonly_fields = ('user',)