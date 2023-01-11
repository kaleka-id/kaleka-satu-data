from django.contrib import admin
from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from .profesi import Profesi
from .alamat import Alamat

class Orang(models.Model):
    class Meta:
        verbose_name = 'Orang'
        verbose_name_plural = 'Orang'
        permissions = [
            ('search_orang', 'Can search Orang in Dictionary')
        ]

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    nik = models.PositiveBigIntegerField(verbose_name='Nomor Induk Kependudukan', unique=True)
    nama_lengkap = models.CharField(max_length=50, help_text='Nama sesuai KTP, tidak ditambahkan gelar.')
    jenis_kelamin = models.CharField(max_length=9, choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')])
    tempat_lahir = models.CharField(max_length=30, help_text='Tulisan akan otomatis terkonversi menjadi huruf kapital.')
    tanggal_lahir = models.DateField()
    status_kawin = models.CharField(max_length=11, choices=[('Belum Kawin', 'Belum Kawin'), ('Kawin', 'Kawin'), ('Cerai Hidup', 'Cerai Hidup'), ('Cerai Mati', 'Cerai Mati')], blank=True, null=True)
    profesi = models.ManyToManyField(Profesi, blank=True)
    rt = models.PositiveSmallIntegerField(verbose_name='RT')
    rw = models.PositiveSmallIntegerField(verbose_name='RW')
    alamat = models.ForeignKey(Alamat, on_delete=models.CASCADE, help_text=mark_safe('Gunakan tabel <a target="blank" href="/dict/alamat/">Alamat</a> sebagai referensi untuk mengisi bagian ini'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_lengkap

    def save(self, *args, **kwargs):
        self.tempat_lahir = self.tempat_lahir.upper()
        return super(Orang, self).save(*args, **kwargs)

@admin.register(Orang)
class OrangModel(admin.ModelAdmin):
    search_fields = ('nama_lengkap', 'nik')
    list_filter = ('jenis_kelamin', 'tempat_lahir', 'tanggal_lahir', 'status_kawin', 'profesi', 'rt', 'rw', 'alamat', 'created_at', 'updated_at', 'user')
    list_display = ('nik', 'nama_lengkap', 'jenis_kelamin', 'tempat_lahir', 'tanggal_lahir', 'status_kawin', 'updated_at', 'user')
    filter_horizontal = ('profesi',)
    raw_id_fields = ('alamat',)
    readonly_fields = ('user',)

    # Decrease pagination for performance in Django Admin
    list_per_page = 25

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()
