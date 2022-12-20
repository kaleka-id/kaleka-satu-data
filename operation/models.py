from django.db import models
# from django.contrib.postgres.fields import array
from django_better_admin_arrayfield.models.fields import ArrayField
import uuid

# Create your models here.
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

class Docs(models.Model):
  class Meta:
    verbose_name = 'Documentation'
    verbose_name_plural = 'Documentations'

  judul = models.CharField(max_length=40)
  gambar = models.FileField(upload_to='docs/')
  deskripsi = models.TextField()
  deskripsi_data = ArrayField(models.TextField())