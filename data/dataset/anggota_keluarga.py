from django.contrib import admin
from django.db import models
import uuid
from django.contrib.auth.models import User
from .orang import Orang
from .keluarga import Keluarga

class AnggotaKeluarga(models.Model):
    class Meta:
        verbose_name = 'Anggota Keluarga'
        verbose_name_plural = 'Anggota Keluarga'
    
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    orang = models.ForeignKey(Orang, on_delete=models.CASCADE)
    keluarga = models.ForeignKey(Keluarga, on_delete=models.CASCADE)
    status_anggota = models.CharField(max_length=7, choices=[('Kepala', 'Kepala'), ('Anggota', 'Anggota')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

@admin.register(AnggotaKeluarga)
class AnggotaKeluargaModel(admin.ModelAdmin):
    search_fields = ('orang',)
    list_filter = ('orang', 'keluarga', 'created_at', 'updated_at')
    list_display = ('id', 'orang', 'keluarga', 'updated_at', 'user')
    raw_id_fields = ('orang', 'keluarga')
    readonly_fields = ('user',)

    # Decrease pagination for performance in Django Admin
    list_per_page = 25

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()