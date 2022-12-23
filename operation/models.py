from django.db import models
from django.contrib.postgres.fields import array, HStoreField
from django_better_admin_arrayfield.models.fields import ArrayField
from django.contrib.auth.models import User
import uuid

# FORMS
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

# DOCS
class Docs(models.Model):
  class Meta:
    verbose_name = 'Documentation'
    verbose_name_plural = 'Documentations'

  judul = models.CharField(max_length=40)
  gambar = models.FileField(upload_to='docs/')
  deskripsi = models.TextField()
  dictionary_data = HStoreField(blank=True, null=True, verbose_name='Dictionary')
  updated_at = models.DateTimeField(auto_now=True)

# DICTIONARY
class Dictionary(models.Model):
  class Meta:
    verbose_name_plural = 'Dictionaries'

  nama = models.CharField(max_length=40)
  url_path = models.CharField(max_length=80, verbose_name='URL Path')
  perms_view = models.CharField(max_length=80, verbose_name='View Permission')

# DASHBOARD
class Dashboard(models.Model):
  nama = models.CharField(max_length=40)
  category = models.CharField(max_length=10, choices=[('Live', 'Live'), ('Analytics', 'Analytics')])
  email_maintainer = models.CharField(max_length=40)
  page_url = models.CharField(max_length=80, verbose_name='Page URL Path')
  embed_url = models.CharField(max_length=100, verbose_name='Embed URL Path')
  width = models.CharField(max_length=8, help_text="Gunakan CSS unit seperti '%', 'cm', 'mm', 'in', 'px', 'pt', dan 'pc'. Contoh: 500px")
  height = models.CharField(max_length=8, help_text="Gunakan CSS unit seperti '%', 'cm', 'mm', 'in', 'px', 'pt', dan 'pc'. Contoh: 500px")
  perms_view = ArrayField(models.PositiveIntegerField(), null=True, blank=True)