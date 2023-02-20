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
  country_code = models.CharField(max_length=5, editable=False, default='N/A')
  country = models.CharField(max_length=80, editable=False, default='None')
  region_code = models.CharField(max_length=5, editable=False, default='N/A')
  region = models.CharField(max_length=80, editable=False, default='None')
  city = models.CharField(max_length=80, editable=False, default='None')
  lat = models.DecimalField(max_digits= 8, decimal_places=4, editable=False, default=0.0)
  lon = models.DecimalField(max_digits= 8, decimal_places=4, editable=False, default=0.0)
  timezone = models.CharField(max_length=20, editable=False, default='None')
  isp = models.CharField(max_length=80, editable=False, default='None')
  isp_detail = models.CharField(max_length=100, editable=False, default='None')

# ACTIVITY LOGS ADMIN
@admin.register(ActivityLog)
class ActivityLogModel(ExportMixin ,admin.ModelAdmin):
  search_fields = ('username',)
  list_display = ('id', 'url_access', 'ip', 'city', 'electronic', 'browser_type', 'timestamp', 'username')
  list_filter = (
    'ip', 'url_access', 'timestamp', 'electronic', 
    'os_type', 'os_version', 'browser_type', 'browser_version', 
    'device_type', 'device_brand', 'device_model', 'username')