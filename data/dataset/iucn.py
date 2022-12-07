from django.contrib import admin
from django.db import models
import uuid
from django.contrib.auth.models import User
from .spesies import Spesies
from .negara import Negara

class IUCN(models.Model):
    class Meta:
        verbose_name = 'IUCN Red List'
        verbose_name_plural = 'IUCN Red List'

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    spesies = models.ForeignKey(Spesies, on_delete=models.CASCADE)
    kategori = models.CharField(max_length=2, 
        choices=[
            ('NE', 'Not Evaluated'),
            ('DD', 'Data Deficient'),
            ('LC', 'Least Concern'),
            ('NT', 'Near Threatened'),
            ('VU', 'Vulnerable'),
            ('EN', 'Endangered'),
            ('CR', 'Critically Endangered'),
            ('EW', 'Extinct in the Wild'),
            ('EX', 'Extinct')
        ]
    )
    tanggal_asesmen = models.DateField()
    referensi_asesmen = models.TextField()
    habitat_asal = models.ManyToManyField(Negara)
    lokasi_geografis = models.TextField(blank=True, help_text='Saat ini tolong diisikan dengan koordinat Well-known Text (WKT) Geografis WGS84. Ke depan akan diganti dengan fitur digitasi spasial')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

@admin.register(IUCN)
class IUCNModel(admin.ModelAdmin):
    search_fields = ('spesies',)
    ordering = ('spesies',)
    list_filter = ('kategori', 'tanggal_asesmen', 'referensi_asesmen', 'habitat_asal', 'created_at', 'updated_at', 'user')
    list_display = ('id', 'spesies', 'kategori', 'tanggal_asesmen', 'referensi_asesmen', 'updated_at', 'user')
    filter_horizontal = ('habitat_asal',)
    raw_id_fields = ('spesies',)
    readonly_fields = ('user',)

    # Decrease pagination for performance in Django Admin
    list_per_page = 25

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()