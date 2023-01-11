from django.contrib import admin
from django.db import models
import uuid
from django.contrib.auth.models import User

class KBJI(models.Model):
    class Meta:
        verbose_name = 'Klasifikasi Baku Jabatan'
        verbose_name_plural = 'Klasifikasi Baku Jabatan'
        permissions = [
            ('search_kbji', 'Can search KBJI in Dictionary')
        ]

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    kode_gol_pokok = models.CharField(max_length=1, verbose_name='Kode Golongan Pokok')
    golongan_pokok = models.CharField(max_length=100, verbose_name='Nama Golongan Pokok', help_text='Tulisan akan otomatis terkonversi menjadi huruf kapital.')
    kode_subgol_pokok = models.CharField(max_length=2, verbose_name='Kode Sub-Golongan Pokok')
    subgolongan_pokok = models.CharField(max_length=100, verbose_name='Nama Sub-Golongan Pokok', help_text='Tulisan akan otomatis terkonversi menjadi huruf kapital.')
    kode_gol = models.CharField(max_length=3, verbose_name='Kode Golongan')
    golongan = models.CharField(max_length=100, verbose_name='Nama Golongan', help_text='Tulisan akan otomatis terkonversi menjadi huruf kapital.')
    kode_subgol = models.CharField(max_length=4, verbose_name='Kode Sub-Golongan')
    subgolongan = models.CharField(max_length=100, verbose_name='Nama Sub-Golongan', help_text='Tulisan akan otomatis terkonversi menjadi huruf kapital.')
    kode_jabatan = models.DecimalField(max_digits=6, decimal_places=2, unique=True, verbose_name='Kode Jabatan')
    jabatan = models.CharField(max_length=100, verbose_name='Nama Jabatan', help_text='Tulisan akan otomatis terkonversi menjadi huruf kapital.')
    dasar_hukum = models.CharField(max_length=120)
    status_data = models.CharField(max_length=11, verbose_name='Status Data', choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.jabatan

@admin.register(KBJI)
class KBJIModel(admin.ModelAdmin):
    search_fields = ('golongan_pokok', 'subgolongan_pokok', 'golongan', 'subgolongan', 'jabatan')
    list_filter = ('kode_gol_pokok', 'kode_subgol_pokok', 'kode_gol', 'kode_subgol', 'kode_jabatan', 'dasar_hukum', 'status_data', 'created_at', 'updated_at', 'user')
    list_display = ('id', 'golongan_pokok', 'subgolongan_pokok', 'golongan', 'subgolongan', 'jabatan', 'status_data', 'updated_at', 'user')
    fieldsets = [
        ('Golongan Pokok', {'fields': ('golongan_pokok', 'kode_gol_pokok')}),
        ('Sub-Golongan Pokok', {'fields': ('subgolongan_pokok', 'kode_subgol_pokok')}),
        ('Golongan', {'fields': ('golongan', 'kode_gol')}),
        ('Sub-Golongan', {'fields': ('subgolongan', 'kode_subgol')}),
        ('Jabatan', {'fields': ('jabatan', 'kode_jabatan')}),
        ('Metadata', {'fields': ('dasar_hukum', 'status_data')})
    ]

    # Decrease pagination for performance in Django Admin
    list_per_page = 25

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()