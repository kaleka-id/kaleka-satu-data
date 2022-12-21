from django.contrib import admin
from django import forms
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django_admin_hstore_widget.forms import HStoreFormField
from .models import *

# Register your models here.
@admin.register(Forms)
class FormModel(admin.ModelAdmin):
  search_fields = ('nama', 'url_alias')
  list_display = ('id', 'nama', 'url_path', 'url_add')

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