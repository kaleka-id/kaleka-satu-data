from django.db import models
from django.contrib import admin

# DICTIONARY MODEL
class Dictionary(models.Model):
  class Meta:
    verbose_name_plural = 'Dictionaries'

  nama = models.CharField(max_length=40)
  url_path = models.CharField(max_length=80, verbose_name='URL Path')
  perms_view = models.CharField(max_length=80, verbose_name='View Permission')

# DICTIONARY ADMIN
@admin.register(Dictionary)
class DictionaryModel(admin.ModelAdmin):
  search_fields = ('nama',)
  list_display = ('id', 'nama', 'url_path')