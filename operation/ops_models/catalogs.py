import os
from django.db import models
from django.contrib import admin
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.postgres.fields import HStoreField
from django_better_admin_arrayfield.models.fields import ArrayField
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django_admin_hstore_widget.forms import HStoreFormField
from data.validators import file_doc
import uuid

# CATALOG MODEL
class Catalog(models.Model):
  def get_filename(instance, filename):
    extension = filename.split('.')[-1]
    unique = uuid.uuid1().hex
    return f'catalog/img/{unique}.{extension}'
  
  nama = models.CharField(max_length=40)
  email_maintainers = ArrayField(models.EmailField(), blank=True, null=True)
  thumbnail = models.ImageField(upload_to=get_filename)
  bigquery_table = HStoreField(models.CharField(max_length=100), blank=True, null=True)
  google_sheets = HStoreField(models.URLField(), null=True, blank=True)
  permission_view = models.ForeignKey(to=Group, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.nama

# CATALOG FORM
class CatalogForm(forms.ModelForm):
  class Meta:
    model = Catalog
    exclude = ()
  
  bigquery_table = HStoreFormField()
  google_sheets = HStoreFormField()
    

# CATALOGS ADMIN
@admin.register(Catalog)
class CatalogModel(admin.ModelAdmin, DynamicArrayMixin):
  search_fields = ('nama',)
  list_display = ('id', 'nama', 'email_maintainers', 'permission_view')
  form = CatalogForm

# CATALOG DOCUMENT MODEL
class CatalogDocument(models.Model):
  catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
  documents = models.FileField(upload_to='catalog/docs', validators=[file_doc])
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def filename(self):
    return os.path.basename(self.documents.name)

  def extension(self):
    name, extension = os.path.splitext(self.documents.name)
    return extension

# CATALOGS DOCUMENT ADMIN
@admin.register(CatalogDocument)
class CatalogDocumentModel(admin.ModelAdmin, DynamicArrayMixin):
  search_fields = ('nama',)
  list_display = ('id', 'catalog', 'user')
  raw_id_fields = ('catalog',)
  readonly_fields = ('user',)

  def save_model(self, request, obj, form, change): 
    obj.user = request.user
    obj.save()