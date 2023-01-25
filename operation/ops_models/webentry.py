from django.db import models
from django.contrib import admin

# WEB ENTRY MODEL
class WebEntry(models.Model):
  class Meta:
    verbose_name_plural = 'Web Entries'

  action = models.CharField(max_length=50, editable=False)
  ip = models.GenericIPAddressField(null=True, editable=False)
  timestamp = models.DateTimeField(auto_now_add=True, editable=False)
  username = models.CharField(max_length=50, editable=False)

# WEB ENTRY ADMIN
@admin.register(WebEntry)
class WebEntryModel(admin.ModelAdmin):
  search_fields = ('username',)
  list_display = ('id', 'ip', 'action', 'timestamp', 'username')
  list_filter = ('ip', 'action', 'timestamp', 'username')