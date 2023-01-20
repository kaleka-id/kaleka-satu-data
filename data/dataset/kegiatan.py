from django.contrib import admin
from django.db import models
import uuid
from django.contrib.auth.models import User 
from django.utils.safestring import mark_safe
from data.dataset.orang import Orang
from import_export.admin import ImportExportModelAdmin

# 🚨KEGIATAN🚨
class Kegiatan(models.Model):
  class Meta:
    verbose_name = 'Kegiatan'
    verbose_name_plural = 'Kegiatan'
    permissions = [
      ('search_kegiatan', 'Can search Kegiatan in Dictionary')
    ]

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  nama = models.CharField(max_length=200, verbose_name='Nama Kegiatan')
  tanggal_mulai = models.DateField(verbose_name='Tanggal Mulai Kegiatan')
  tanggal_selesai = models.DateField(verbose_name='Tanggal Selesai Kegiatan')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.nama
  
@admin.register(Kegiatan)
class KegiatanModel(ImportExportModelAdmin):
  search_fields = ('nama',)
  ordering = ('nama',)
  list_filter = ('tanggal_mulai', 'tanggal_selesai', 'created_at', 'updated_at', 'user')
  list_display = ('id', 'nama', 'tanggal_mulai', 'tanggal_selesai', 'updated_at', 'user')
  list_per_page = 25

  def save_model(self, request, obj, form, change): 
    obj.user = request.user
    obj.save()

# 🚨PESERTA KEGIATAN🚨
class PesertaKegiatan(models.Model):
  class Meta:
    verbose_name = 'Peserta Kegiatan'
    verbose_name_plural = 'Peserta Kegiatan'
  
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  kegiatan = models.ForeignKey(Kegiatan, on_delete=models.CASCADE, help_text=mark_safe('Gunakan tabel <a target="blank" href="/dict/kegiatan/">Kegiatan</a> sebagai referensi untuk mengisi bagian ini'))
  peserta = models.ForeignKey(Orang, on_delete=models.CASCADE, help_text=mark_safe('Gunakan tabel <a target="blank" href="/dict/orang/">Orang</a> sebagai referensi untuk mengisi bagian ini'))
  status_kehadiran = models.CharField(max_length=10, choices=[('Peserta', 'Peserta'), ('Narasumber', 'Narasumber'), ('Panitia', 'Panitia')])
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

@admin.register(PesertaKegiatan)
class PesertaKegiatanModel(ImportExportModelAdmin):
  ordering = ('kegiatan',)
  list_filter = ('kegiatan', 'peserta', 'status_kehadiran', 'created_at', 'updated_at', 'user')
  list_display = ('id', 'kegiatan', 'peserta', 'status_kehadiran', 'updated_at', 'user')
  raw_id_fields = ('peserta', 'kegiatan')
  list_per_page = 25

  def save_model(self, request, obj, form, change): 
    obj.user = request.user
    obj.save()

# 🚨FOTO KEGIATAN🚨
class FotoKegiatan(models.Model):
  class Meta:
    verbose_name = 'Foto Kegiatan'
    verbose_name_plural = 'Foto Kegiatan'

  def get_filename(instance, filename):
    extension = filename.split('.')[-1]
    unique = uuid.uuid1().hex
    return f'dataset/kegiatan/foto/{unique}.{extension}'

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  kegiatan = models.ForeignKey(Kegiatan, on_delete=models.CASCADE)
  foto = models.ImageField(upload_to=get_filename)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

@admin.register(FotoKegiatan)
class FotoKegiatanModel(admin.ModelAdmin):
  ordering = ('kegiatan',)
  list_filter = ('kegiatan', 'created_at', 'updated_at', 'user')
  list_display = ('id', 'kegiatan', 'updated_at', 'user')
  raw_id_fields = ('kegiatan',)
  list_per_page = 25

  def save_model(self, request, obj, form, change): 
    obj.user = request.user
    obj.save()
