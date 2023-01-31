from django.db import models
from django.contrib import admin
from django.contrib.auth.models import Group
from django_better_admin_arrayfield.models.fields import ArrayField
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

# DASHBOARD MODEL
class Dashboard(models.Model):
  nama = models.CharField(max_length=40)
  category = models.CharField(max_length=20, choices=[('Static CSV', 'Static CSV'), ('Google Sheets', 'Google Sheets'), ('Google BigQuery', 'Google BigQuery'), ('Amazon Redshift', 'Amazon Redshift'), ('PostgreSQL Database', 'PostgreSQL Database'), ('MySQL Database', 'MySQL Database')])
  email_maintainers = ArrayField(models.EmailField(), blank=True, null=True)
  page_url = models.CharField(max_length=80, verbose_name='Page URL Path')
  embed_url = models.URLField(max_length=100, verbose_name='Embed URL Path')
  width = models.CharField(max_length=8, help_text="Gunakan CSS unit seperti '%', 'cm', 'mm', 'in', 'px', 'pt', dan 'pc'. Contoh: 500px")
  height = models.CharField(max_length=8, help_text="Gunakan CSS unit seperti '%', 'cm', 'mm', 'in', 'px', 'pt', dan 'pc'. Contoh: 500px")
  permission_view = models.ForeignKey(to=Group, on_delete=models.CASCADE, null=True)

# DASHBOARDS ADMIN
@admin.register(Dashboard)
class DashboardModel(admin.ModelAdmin, DynamicArrayMixin):
  search_fields = ('nama',)
  list_display = ('id', 'nama', 'category', 'email_maintainers', 'permission_view')