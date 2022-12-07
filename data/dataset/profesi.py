from django.contrib import admin
from django.db import models
import uuid
from django.contrib.auth.models import User
from .kbji import KBJI

class Profesi(models.Model):
    class Meta:
        verbose_name = 'Profesi'
        verbose_name_plural = 'Profesi'

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    nama = models.CharField(max_length=50)
    kode_kbji = models.ForeignKey(KBJI, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama

@admin.register(Profesi)
class ProfesiModel(admin.ModelAdmin):
    search_fields = ('nama',)
    list_filter = ('kode_kbji', 'created_at', 'updated_at', 'user')
    list_display = ('id', 'nama', 'kode_kbji', 'updated_at', 'user')
    raw_id_fields = ('kode_kbji',)
    readonly_fields = ('user',)

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()