from django.db import models
from django.contrib import admin
from import_export.admin import ExportMixin

# DATA LOGS MODEL
class DataLog(models.Model):
  action = models.CharField(max_length=10, editable=False)
  dataset = models.CharField(max_length=100, editable=False)
  id_dataset = models.CharField(max_length=50, editable=False)
  user = models.CharField(max_length=50, editable=False)
  ip_user = models.CharField(max_length=50, editable=False)
  device_user = models.CharField(max_length=100, editable=False)
  os_user = models.CharField(max_length=100, editable=False)
  browser_user = models.CharField(max_length=100, editable=False)
  timestamp = models.DateTimeField(auto_now_add=True)

# DATA LOGS ADMIN
@admin.register(DataLog)
class DictionaryModel(ExportMixin, admin.ModelAdmin):
  search_fields = ('dataset',)
  list_display = ('id', 'action', 'dataset', 'user', 'ip_user', 'timestamp')