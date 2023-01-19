from django.contrib import admin
from django.db import models
import uuid
from django.contrib.auth.models import User
from .alamat import Alamat
from import_export.admin import ImportExportModelAdmin

class KodePos(models.Model):
    class Meta:
        verbose_name = 'Kode Pos'
        verbose_name_plural = 'Kode Pos'
    
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    kode = models.CharField(max_length=5)
    alamat = models.ForeignKey(Alamat, on_delete=models.CASCADE)
    dasar_hukum = models.CharField(max_length=30, verbose_name='Dasar Hukum')
    status_data = models.CharField(max_length=11, verbose_name='Status Data', choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.kode

@admin.register(KodePos)
class KodePosModel(ImportExportModelAdmin):
    search_fields = ('kode',)
    list_filter = ('dasar_hukum', 'status_data', 'created_at', 'updated_at', 'user')
    list_display = ('id', 'kode', 'status_data', 'updated_at', 'user')
    raw_id_fields = ('alamat',)
    readonly_fields = ('user',)

    # Decrease pagination for performance in Django Admin
    list_per_page = 25

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()