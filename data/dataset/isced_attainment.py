from django.contrib import admin
from django.db import models
import uuid
from django.contrib.auth.models import User

class ISCED_Attainment(models.Model):
    class Meta:
        verbose_name = 'Klasifikasi Baku Pendidikan'
        verbose_name_plural = 'Klasifikasi Baku Pendidikan'

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    kode_level = models.CharField(max_length=1)
    deskripsi_level = models.TextField()
    kode_category = models.CharField(max_length=2)
    deskripsi_category = models.TextField()
    kode_subcategory = models.CharField(max_length=3)
    deskripsi_subcategory = models.TextField()
    dasar_hukum = models.CharField(max_length=120)
    status_data = models.CharField(max_length=11, verbose_name='Status Data', choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

@admin.register(ISCED_Attainment)
class ISCED_AttainmentModel(admin.ModelAdmin):
    search_fields = ('deskripsi_level', 'deskripsi_category', 'deskripsi_subcategory')
    list_filter = ('kode_level', 'kode_category', 'kode_subcategory', 'dasar_hukum', 'status_data', 'created_at', 'updated_at', 'user')
    list_display = ('id', 'kode_level', 'kode_category', 'kode_subcategory', 'status_data', 'updated_at', 'user')
    ordering = ('kode_subcategory',)
    fieldsets = [
        ('Level', {'fields': ('kode_level', 'deskripsi_level')}),
        ('Category', {'fields': ('kode_category', 'deskripsi_category')}),
        ('Sub-Category', {'fields': ('kode_subcategory', 'deskripsi_subcategory')}),
        ('Metadata', {'fields': ('dasar_hukum', 'status_data')})
    ]

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()