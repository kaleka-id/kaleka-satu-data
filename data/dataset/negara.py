from django.contrib import admin
from django.db import models
import uuid
from django.contrib.auth.models import User

class Negara(models.Model):
    class Meta:
        verbose_name = 'Negara'
        verbose_name_plural = 'Negara'

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    nama_singkat = models.CharField(max_length=100)
    nama_resmi = models.CharField(max_length=100)
    region_pbb = models.CharField(
        max_length= 15,
        verbose_name='Region PBB',
        choices=[
            ('Africa', 'Africa'), 
            ('Americas', 'Americas'), 
            ('Antarctica', 'Antarctica'), 
            ('Asia', 'Asia'), 
            ('Europe', 'Europe'), 
            ('Oceania', 'Oceania') 
        ]) 
        
    subregion = models.CharField(
        max_length= 30, 
        choices=[
            ('Antarctica', 'Antarctica'),
            ('Australia and New Zealand', 'Australia and New Zealand'),
            ('Caribbean', 'Caribbean'),
            ('Central America', 'Central America'),
            ('Central Asia', 'Central Asia'),
            ('Eastern Africa', 'Eastern Africa'),
            ('Eastern Asia', 'Eastern Asia'),
            ('Eastern Europe', 'Eastern Europe'),
            ('Melanesia', 'Melanesia'),
            ('Micronesia', 'Micronesia'),
            ('Middle Africa', 'Middle Africa'),
            ('Northern Africa', 'Northern Africa'),
            ('Northern America', 'Northern America'),
            ('Northern Europe', 'Northern Europe'),
            ('Polynesia', 'Polynesia'),
            ('Seven seas (open ocean)', 'Seven seas (open ocean)'),
            ('South America', 'South America'),
            ('South-Eastern Asia', 'South-Eastern Asia'),
            ('Southern Africa', 'Southern Africa'),
            ('Southern Asia', 'Southern Asia'),
            ('Southern Europe', 'Southern Europe'),
            ('Western Africa', 'Western Africa'),
            ('Western Asia', 'Western Asia'),
            ('Western Europe', 'Western Europe') 
        ])
    region_wb = models.CharField(
        max_length= 30, 
        verbose_name='Region World Bank', 
        choices=[
             ('Antarctica', 'Antarctica'),
             ('East Asia & Pacific', 'East Asia & Pacific'),
             ('Europe & Central Asia', 'Europe & Central Asia'),
             ('Latin America & Caribbean', 'Latin America & Caribbean'),
             ('Middle East & North Africa', 'Middle East & North Africa'),
             ('North America', 'North America'),
             ('South Asia', 'South Asia'),
             ('Sub-Saharan Africa', 'Sub-Saharan Africa') 
        ])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dasar_hukum = models.CharField(max_length=120)
    status_data = models.CharField(max_length=11, verbose_name='Status Data', choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_singkat

@admin.register(Negara)
class NegaraModel(admin.ModelAdmin):
    search_fields = ('nama_singkat', 'nama_resmi')
    list_filter = ('region_pbb', 'region_wb', 'subregion', 'dasar_hukum', 'status_data', 'created_at', 'updated_at', 'user')
    list_display = ('id', 'nama_singkat', 'region_pbb', 'region_wb', 'subregion', 'status_data', 'updated_at', 'user')
    ordering = ('nama_singkat',)
    readonly_fields = ('user',)

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()