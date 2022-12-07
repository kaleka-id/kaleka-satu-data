from django.contrib import admin
from django.db import models
import uuid
from django.contrib.auth.models import User

class SITC(models.Model):
    class Meta:
        verbose_name = 'Klasifikasi Baku Komoditas'
        verbose_name_plural = 'Klasifikasi Baku Komoditas'

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    kode_section = models.CharField(max_length=1)
    kode_division = models.CharField(max_length=2)
    kode_group = models.CharField(max_length=3)
    kode_subgroup = models.CharField(max_length=5)
    kode_heading = models.CharField(max_length=6)
    deskripsi_section = models.TextField()
    deskripsi_division	= models.TextField()
    deskripsi_group = models.TextField()
    deskripsi_subgroup = models.TextField()
    deskripsi_heading = models.TextField()
    dasar_hukum = models.CharField(max_length=120)
    status_data = models.CharField(max_length=11, verbose_name='Status Data', choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


@admin.register(SITC)
class SITCModel(admin.ModelAdmin):
    search_fields = ('deskripsi_section', 'deskripsi_division', 'deskripsi_group', 'deskripsi_subgroup', 'deskripsi_heading')
    list_filter = ('kode_section', 'kode_division', 'kode_group', 'kode_subgroup', 'kode_heading', 'dasar_hukum', 'status_data', 'created_at', 'updated_at', 'user')
    list_display = ('id', 'kode_section', 'kode_division', 'kode_group', 'kode_subgroup', 'kode_heading', 'status_data', 'updated_at', 'user')
    ordering = ('kode_heading',)
    fieldsets = [
        ('Section', {'fields': ('kode_section', 'deskripsi_section')}),
        ('Division', {'fields': ('kode_division', 'deskripsi_division')}),
        ('Group', {'fields': ('kode_group', 'deskripsi_group')}),
        ('Subgroup', {'fields': ('kode_subgroup', 'deskripsi_subgroup')}),
        ('Heading', {'fields': ('kode_heading', 'deskripsi_heading')}),
        ('Metadata', {'fields': ('dasar_hukum', 'status_data')})
    ]

    # Decrease pagination for performance in Django Admin
    list_per_page = 25

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()