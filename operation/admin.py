from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Forms)
class FormModel(admin.ModelAdmin):
  search_fields = ('nama', 'url_alias')
  list_display = ('id', 'nama', 'url_path', 'url_add')