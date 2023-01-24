from django.db import models
from django.contrib import admin
from django_better_admin_arrayfield.models.fields import ArrayField
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

# CATALOG MODEL
class Catalog(models.Model):
  nama = models.CharField(max_length=40)
  email_maintainer = models.CharField(max_length=40)
  page_url = models.CharField(max_length=80, verbose_name='Page URL Path')
  embed_url = models.URLField(max_length=200, verbose_name='Embed URL Path')
  spreadsheet_url = models.URLField(max_length=200, verbose_name='Google Sheets URL Path')
  width = models.CharField(max_length=8, help_text="Gunakan CSS unit seperti '%', 'cm', 'mm', 'in', 'px', 'pt', dan 'pc'. Contoh: 500px")
  height = models.CharField(max_length=8, help_text="Gunakan CSS unit seperti '%', 'cm', 'mm', 'in', 'px', 'pt', dan 'pc'. Contoh: 500px")
  perms_view = ArrayField(models.CharField(max_length=30), null=True, blank=True)

# CATALOGS ADMIN
@admin.register(Catalog)
class CatalogModel(admin.ModelAdmin, DynamicArrayMixin):
  search_fields = ('nama',)
  list_display = ('id', 'nama', 'email_maintainer', 'perms_view')