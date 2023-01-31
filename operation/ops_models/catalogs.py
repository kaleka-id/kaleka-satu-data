from django.db import models
from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.postgres.fields import HStoreField
from django_better_admin_arrayfield.models.fields import ArrayField
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django_admin_hstore_widget.forms import HStoreFormField

# CATALOG MODEL
class Catalog(models.Model):
  nama = models.CharField(max_length=40)
  email_maintainers = ArrayField(models.EmailField(), blank=True, null=True)
  spreadsheets_download = HStoreField(models.URLField(), blank=True, null=True)
  bigquery_table = HStoreField(models.CharField(max_length=100), blank=True, null=True)
  documents_portable = HStoreField(models.URLField(), blank=True, null=True)
  documents_document = HStoreField(models.URLField(), blank=True, null=True)
  documents_presentation = HStoreField(models.URLField(), blank=True, null=True)
  permission_view = models.ForeignKey(to=Group, on_delete=models.CASCADE, null=True)

# CATALOG FORM
class CatalogForm(forms.ModelForm):
  class Meta:
    model = Catalog
    exclude = ()
  
  spreadsheets_download = HStoreFormField()
  bigquery_table = HStoreFormField()
  documents_portable = HStoreFormField()
  documents_document = HStoreFormField()
  documents_presentation = HStoreFormField()
    

# CATALOGS ADMIN
@admin.register(Catalog)
class CatalogModel(admin.ModelAdmin, DynamicArrayMixin):
  search_fields = ('nama',)
  list_display = ('id', 'nama', 'email_maintainers', 'permission_view')
  form = CatalogForm