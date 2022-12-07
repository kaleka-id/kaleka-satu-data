from django.contrib import admin
from django.db import models
import uuid
from django.contrib.auth.models import User

class Spesies(models.Model):
    class Meta:
        verbose_name = 'Klasifikasi Baku Spesies'
        verbose_name_plural = 'Klasifikasi Baku Spesies'

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    nama_indonesia = models.CharField(max_length=50, blank=True)
    nama_inggris = models.CharField(max_length=50, blank=True)
    kingdom = models.CharField(max_length=50)
    phylum = models.CharField(max_length=50)
    Class = models.CharField(max_length=50)
    order = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    genus = models.CharField(max_length=50)
    species = models.CharField(max_length=100)
    dasar_hukum = models.CharField(max_length=60)
    status_data = models.CharField(max_length=11, verbose_name='Status Data', choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.species

@admin.register(Spesies)
class SpesiesModel(admin.ModelAdmin):
    search_fields = ('nama_indonesia', 'nama_inggris', 'kingdom', 'phylum', 'Class', 'order', 'family', 'genus', 'species')
    list_filter = ('nama_indonesia', 'nama_inggris', 'kingdom', 'phylum', 'Class', 'order', 'family', 'genus', 'species', 'dasar_hukum', 'status_data', 'created_at', 'updated_at', 'user')
    list_display = ('id', 'nama_indonesia', 'kingdom', 'phylum', 'Class', 'order', 'family', 'genus', 'species', 'status_data', 'updated_at', 'user')
    readonly_fields = ('user',)

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()