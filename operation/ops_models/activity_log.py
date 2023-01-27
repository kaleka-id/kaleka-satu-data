from django.db import models
from django.contrib import admin
from import_export.admin import ExportMixin

# ACTIVITY LOGS MODEL
class ActivityLog(models.Model):
  url_access = models.URLField(editable=False)
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

# ACTIVITY LOGS ADMIN
@admin.register(ActivityLog)
class ActivityLogModel(ExportMixin ,admin.ModelAdmin):
  search_fields = ('username',)
  list_display = ('id', 'url_access', 'ip', 'electronic', 'browser_type', 'timestamp', 'username')
  list_filter = (
    'ip', 'url_access', 'timestamp', 'electronic', 
    'os_type', 'os_version', 'browser_type', 'browser_version', 
    'device_type', 'device_brand', 'device_model', 'username')