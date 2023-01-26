from django import forms
from django.db import models
from django.contrib import admin
from django.contrib.postgres.fields import HStoreField
from django_admin_hstore_widget.forms import HStoreFormField
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
import uuid

# DOCS MODEL
class Docs(models.Model):
  class Meta:
    verbose_name = 'Documentation'
    verbose_name_plural = 'Documentations'

  def get_filename(instance, filename):
    extension = filename.split('.')[-1]
    unique = uuid.uuid1().hex
    return f'docs/{unique}.{extension}'

  judul = models.CharField(max_length=40)
  gambar = models.FileField(upload_to=get_filename)
  deskripsi = models.TextField()
  dictionary_data = HStoreField(blank=True, null=True, verbose_name='Dictionary')
  updated_at = models.DateTimeField(auto_now=True)

# DOCS FORM
class DocsModelForm(forms.ModelForm):
  dictionary_data = HStoreFormField()
  
  class Meta:
      model = Docs
      exclude = ()

# DOCS ADMIN
@admin.register(Docs)
class DocsModel(admin.ModelAdmin, DynamicArrayMixin):
  search_fields = ('judul',)
  list_display = ('id', 'judul', 'deskripsi')

  form = DocsModelForm