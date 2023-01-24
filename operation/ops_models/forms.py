from django.db import models
import uuid
from django.contrib import admin

# FORMS MODEL
class Forms(models.Model):
  class Meta:
    verbose_name = 'Form'
    verbose_name_plural = 'Forms'

  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  nama = models.CharField(max_length=40, verbose_name='Nama Form')
  url_path = models.CharField(max_length=80, verbose_name='URL Path')
  url_add = models.CharField(max_length=80, verbose_name='URL Tambah Data')
  perms_view = models.CharField(max_length=80, verbose_name='View Permission')
  perms_add = models.CharField(max_length=80, verbose_name='Add Permission')

# FORMS ADMIN
@admin.register(Forms)
class FormModel(admin.ModelAdmin):
  search_fields = ('nama', )
  list_display = ('id', 'nama', 'url_path', 'url_add')