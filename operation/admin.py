from django.contrib import admin
from django import forms
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django_admin_hstore_widget.forms import HStoreFormField
from .models import *

# FORMS
@admin.register(Forms)
class FormModel(admin.ModelAdmin):
  search_fields = ('nama', )
  list_display = ('id', 'nama', 'url_path', 'url_add')

# DOCS
class DocsModelForm(forms.ModelForm):
    dictionary_data = HStoreFormField()
    
    class Meta:
       model = Docs
       exclude = ()

@admin.register(Docs)
class DocsModel(admin.ModelAdmin, DynamicArrayMixin):
  search_fields = ('judul',)
  list_display = ('id', 'judul', 'deskripsi')

  form = DocsModelForm

# DICTIONARY
@admin.register(Dictionary)
class DictionaryModel(admin.ModelAdmin):
  search_fields = ('nama',)
  list_display = ('id', 'nama', 'url_path')

# DASHBOARDS
@admin.register(Dashboard)
class DashboardModel(admin.ModelAdmin, DynamicArrayMixin):
  search_fields = ('nama',)
  list_display = ('id', 'nama', 'category', 'email_maintainer', 'perms_view')

# CATALOGS
@admin.register(Catalog)
class CatalogModel(admin.ModelAdmin, DynamicArrayMixin):
  search_fields = ('nama',)
  list_display = ('id', 'nama', 'email_maintainer', 'perms_view')