from django.contrib import admin
from django.db import models
import uuid
from django.contrib.auth.models import User
from .alamat import Alamat
from import_export.admin import ImportExportModelAdmin

class Keluarga(models.Model):
    class Meta:
        verbose_name = 'Keluarga'
        verbose_name_plural = 'Keluarga'

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    nkk = models.PositiveBigIntegerField(verbose_name='Nomor Kartu Kependudukan', unique=True)
    rt = models.PositiveSmallIntegerField(verbose_name='RT')
    rw = models.PositiveSmallIntegerField(verbose_name='RW')
    alamat = models.ForeignKey(Alamat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nkk)

@admin.register(Keluarga)
class KeluargaModel(ImportExportModelAdmin):
    search_fields = ('nkk',)
    list_filter = ('rt', 'rw', 'alamat', 'created_at', 'updated_at', 'user')
    list_display = ('nkk', 'updated_at', 'user')
    raw_id_fields = ('alamat',)
    readonly_fields = ('user',)

    # Decrease pagination for performance in Django Admin
    list_per_page = 25

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()