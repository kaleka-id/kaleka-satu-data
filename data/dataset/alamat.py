from django.contrib import admin
from django.db import models
import uuid
from django.contrib.auth.models import User

class Alamat(models.Model):
    class Meta:
        verbose_name = 'Alamat'
        verbose_name_plural = 'Alamat'

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    kode_prov = models.CharField(max_length=2, verbose_name='Kode Provinsi')
    nama_prov = models.CharField(max_length=30, verbose_name='Nama Provinsi', help_text="Tuliskan nama provinsi tanpa imbuhan 'Provinsi', 'Prov.' dsb. Tulisan akan otomatis terkonversi menjadi huruf kapital.")
    kode_kabkot = models.CharField(max_length=4, verbose_name='Kode Kabupaten/Kota')
    nama_kabkot = models.CharField(max_length=30, verbose_name='Nama Kabupaten/Kota', help_text="Tuliskan nama kabupaten tanpa imbuhan 'Kabupaten', 'Kab.' dsb. Untuk nama kota, gunakan imbuhan 'Kota'. Tulisan akan otomatis terkonversi menjadi huruf kapital.")
    kode_kec = models.CharField(max_length=6, verbose_name='Kode Kecamatan')
    nama_kec = models.CharField(max_length=40, verbose_name='Nama Kecamatan', help_text="Tuliskan nama kecamatan tanpa imbuhan 'Kecamatan', 'Kec.' dsb. Tulisan akan otomatis terkonversi menjadi huruf kapital.")
    kode_desa = models.CharField(max_length=10, unique=True, verbose_name='Kode Desa/Kelurahan')
    nama_desa = models.CharField(max_length=40, verbose_name='Nama Desa/Kelurahan', help_text="Tuliskan nama desa tanpa imbuhan 'Desa', 'Ds.' dsb. Untuk nama kelurahan, gunakan imbuhan 'Kel.'. Tulisan akan otomatis terkonversi menjadi huruf kapital.")
    dasar_hukum = models.CharField(max_length=30, verbose_name='Dasar Hukum')
    status_data = models.CharField(max_length=11, verbose_name='Status Data', choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_desa
    
    def save(self, *args, **kwargs):
        self.nama_prov = self.nama_prov.upper()
        self.nama_kabkot = self.nama_kabkot.upper()
        self.nama_kec = self.nama_kec.upper()
        self.nama_desa = self.nama_desa.upper()
        return super(Alamat, self).save(*args, **kwargs)

@admin.register(Alamat)
class AlamatModel(admin.ModelAdmin):
    search_fields = ('nama_prov', 'nama_kabkot', 'nama_kec', 'nama_desa')
    ordering = ('kode_desa',)
    list_filter = ('kode_prov', 'nama_prov', 
        'kode_kabkot', 'nama_kabkot', 
        'kode_kec', 'nama_kec',
        'kode_desa', 'nama_desa',
        'dasar_hukum', 'status_data',
        'created_at', 'updated_at', 'user')
    list_display = ('id', 'nama_prov', 'nama_kabkot', 'nama_kec', 'nama_desa', 'status_data', 'updated_at', 'user')
    fieldsets = [
        ('Provinsi', {'fields': ('kode_prov', 'nama_prov')}),
        ('Kabupaten/Kota', {'fields': ('kode_kabkot', 'nama_kabkot')}),
        ('Kecamatan', {'fields': ('kode_kec', 'nama_kec')}),
        ('Desa/Kelurahan', {'fields': ('kode_desa', 'nama_desa')}),
        ('Metadata', {'fields': ('dasar_hukum', 'status_data')})
    ]

    # Decrease pagination for performance in Django Admin
    list_per_page = 25

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()