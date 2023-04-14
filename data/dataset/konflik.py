from django.contrib import admin
from django.db import models
import uuid
from django.contrib.auth.models import User 
from django.utils.safestring import mark_safe
from data.dataset.orang import Orang
from data.dataset.alamat import Alamat
from data.dataset.organisasi import Organisasi
from import_export.admin import ImportExportModelAdmin
from django_better_admin_arrayfield.models.fields import ArrayField

# 🚨KONFLIK🚨
class Konflik(models.Model):
  class Meta:
    verbose_name = 'Konflik'
    verbose_name_plural = 'Konflik'
    permissions = [
      ('search_konflik', 'Can search Konflik in Dictionary')
    ]

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  no_registrasi = models.CharField(max_length=30, unique=True)
  status = models.CharField(max_length=15)
  tahun = models.SmallIntegerField()
  lokasi = models.ForeignKey(Alamat, on_delete=models.CASCADE)
  interviewer = models.ForeignKey(Orang, on_delete=models.CASCADE)
  tipologi = models.CharField(max_length=70)
  status_data = models.CharField(max_length=20, choices=[('Updated', 'Updated'), ('Need Confirmation', 'Need Confirmation'), ('Not Valid', 'Not Valid')], default='Need Confirmation')
  keterangan = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.no_registrasi
  
@admin.register(Konflik)
class KonflikModel(ImportExportModelAdmin):
  search_fields = ('no_registrasi',)
  raw_id_fields = ('lokasi', 'interviewer')
  list_filter = ('status', 'tahun', 'tipologi', 'status_data', 'updated_at', 'user')
  list_display = ('no_registrasi', 'status', 'tipologi', 'updated_at', 'user')
  list_per_page = 25

  def save_model(self, request, obj, form, change): 
    obj.user = request.user
    obj.save()

# 🚨KONFLIK DETAIL🚨
class KonflikDetail(models.Model):
  class Meta:
    verbose_name = 'Konflik - Detail'
    verbose_name_plural = 'Konflik - Detail'

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  konflik = models.OneToOneField(Konflik, on_delete=models.CASCADE)
  status_lahan = models.CharField(max_length=20)
  alasan_hak = models.CharField(max_length=20)
  alasan_konflik = models.TextField()
  luas_konflik = models.DecimalField(max_digits=8, decimal_places=2)
  tuntutan = models.TextField()
  pernah_diselesaikan = models.BooleanField()
  waktu_penyelesaian = models.DateField()
  mediator = ArrayField(models.CharField(max_length=20))
  upaya_penyelesaian = models.TextField()
  penyelesaian_akhir = models.TextField(null=True, blank=True)
  catatan = models.TextField(null=True, blank=True)
  status_data = models.CharField(max_length=20, choices=[('Updated', 'Updated'), ('Need Confirmation', 'Need Confirmation'), ('Not Valid', 'Not Valid')], default='Need Confirmation')
  keterangan = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

@admin.register(KonflikDetail)
class KonflikDetailModel(ImportExportModelAdmin):
  list_per_page = 25

  def save_model(self, request, obj, form, change): 
    obj.user = request.user
    obj.save()

# 🚨KONFLIK PELAPOR🚨
class KonflikPelapor(models.Model):
  class Meta:
    verbose_name = 'Konflik - Pelapor'
    verbose_name_plural = 'Konflik - Pelapor'

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  konflik = models.OneToOneField(Konflik, on_delete=models.CASCADE)
  status = models.CharField(max_length=20, choices=[('Individu', 'Individu'), ('Kelompok', 'Kelompok')])
  pelapor_individu = models.ForeignKey(Orang, on_delete=models.CASCADE, null=True, blank=True, help_text=mark_safe('Diisi jika statusnya <b>Individu</b>'))
  pelapor_kelompok = models.ForeignKey(Organisasi, on_delete=models.CASCADE, null=True, blank=True, help_text=mark_safe('Diisi jika statusnya <b>Kelompok</b>'))
  alamat = models.ForeignKey(Alamat, on_delete=models.CASCADE)
  keluarga_terdampak = models.PositiveSmallIntegerField()
  status_data = models.CharField(max_length=20, choices=[('Updated', 'Updated'), ('Need Confirmation', 'Need Confirmation'), ('Not Valid', 'Not Valid')], default='Need Confirmation')
  keterangan = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

@admin.register(KonflikPelapor)
class KonflikPelaporModel(ImportExportModelAdmin):
  list_per_page = 25

  def save_model(self, request, obj, form, change): 
    obj.user = request.user
    obj.save()

# 🚨KONFLIK TERLAPOR🚨
class KonflikTerlapor(models.Model):
  class Meta:
    verbose_name = 'Konflik - Terlapor'
    verbose_name_plural = 'Konflik - Terlapor'

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  konflik = models.OneToOneField(Konflik, on_delete=models.CASCADE)
  status = models.CharField(max_length=20, choices=[('Individu', 'Individu'), ('Kelompok', 'Kelompok')])
  terlapor_individu = models.ForeignKey(Orang, on_delete=models.CASCADE, null=True, blank=True, help_text=mark_safe('Diisi jika statusnya <b>Individu</b>'))
  terlapor_kelompok = models.ForeignKey(Organisasi, on_delete=models.CASCADE, null=True, blank=True, help_text=mark_safe('Diisi jika statusnya <b>Kelompok</b>'))
  alamat = models.ForeignKey(Alamat, on_delete=models.CASCADE)
  status_data = models.CharField(max_length=20, choices=[('Updated', 'Updated'), ('Need Confirmation', 'Need Confirmation'), ('Not Valid', 'Not Valid')], default='Need Confirmation')
  keterangan = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

@admin.register(KonflikTerlapor)
class KonflikTerlaporModel(ImportExportModelAdmin):
  list_per_page = 25

  def save_model(self, request, obj, form, change): 
    obj.user = request.user
    obj.save()