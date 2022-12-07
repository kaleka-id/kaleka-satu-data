from django.contrib import admin
from django.db import models
import uuid
from django.contrib.auth.models import User

class Testing(models.Model):
    class Meta:
        verbose_name = 'Testing Data'
        verbose_name_plural = 'Testing Data'

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    kode = models.CharField(max_length=5)
    nama = models.CharField(max_length=30)
    deskripsi = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama

@admin.register(Testing)
class TestingModel(admin.ModelAdmin):
    search_fields = ('kode', 'nama')
    list_filter = ('kode', 'nama', 'created_at', 'updated_at', 'user')
    list_display = ('id', 'kode', 'nama', 'created_at', 'updated_at', 'user')
    readonly_fields = ('user',)

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()