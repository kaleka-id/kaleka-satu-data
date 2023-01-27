from django.db import models
from django.contrib import admin
from import_export.admin import ExportMixin

# WEB ENTRY MODEL
class WebEntry(models.Model):
  class Meta:
    verbose_name_plural = 'Web entries'

  action = models.CharField(max_length=50, editable=False)
  ip = models.GenericIPAddressField(null=True, editable=False)
  timestamp = models.DateTimeField(auto_now_add=True, editable=False)
  electronic = models.CharField(max_length=50, editable=False)
  is_touchscreen = models.BooleanField(editable=False)
  is_bot = models.BooleanField(editable=False)
  os_type = models.CharField(max_length=50, editable=False)
  os_version = models.CharField(max_length=50, editable=False)
  browser_type = models.CharField(max_length=50, editable=False)
  browser_version = models.CharField(max_length=50, editable=False)
  device_type = models.CharField(max_length=50, editable=False)
  device_brand = models.CharField(max_length=50, editable=False)
  device_model = models.CharField(max_length=50, editable=False)
  username = models.CharField(max_length=50, editable=False)

# WEB ENTRY ADMIN
@admin.register(WebEntry)
class WebEntryModel(ExportMixin ,admin.ModelAdmin):
  search_fields = ('username',)
  list_display = ('id', 'ip', 'electronic', 'browser_type', 'action', 'timestamp', 'username')
  list_filter = (
    'ip', 'action', 'timestamp', 'electronic', 
    'os_type', 'os_version', 'browser_type', 'browser_version', 
    'device_type', 'device_brand', 'device_model', 'username')