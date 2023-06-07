from django.db import models
from django.contrib.postgres import fields as pgModels
from django.contrib import admin
from django.contrib.auth.models import User
from import_export.admin import ExportMixin

# REQUEST MODEL
class Request(models.Model):
  subject = models.CharField(max_length=100)
  request_type = models.CharField(max_length=50, choices=[
    ('Add Catalog', 'Add Catalog'),
    ('Add Dashboard', 'Add Dashboard'),
    ('Add Dataset', 'Add Dataset'),
    ('Add Dictionary', 'Add Dictionary'),
    ('Add Form', 'Add Form'),
    ('Add Dictionary', 'Add Dictionary'),
    ('Modify Catalog', 'Modify Catalog'),
    ('Modify Dashboard', 'Modify Dashboard'),
    ('Modify Dataset', 'Modify Dataset'),
    ('Modify Dictionary', 'Modify Dictionary'),
    ('Modify Form', 'Modify Form'),
    ('Modify Dictionary', 'Modify Dictionary'),
    ('Bug Report', 'Bug Report'),
  ])
  message = models.TextField()
  status = models.CharField(max_length=10, choices=[
    ('Pending', 'Pending'), 
    ('Process', 'Process'), 
    ('Complete', 'Complete'), 
    ('Decline', 'Decline')], default='Pending')
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

# REQUEST ADMIN
@admin.register(Request)
class RequestModel(ExportMixin, admin.ModelAdmin):
  search_fields = ('subject',)
  list_display = ('subject', 'request_type', 'status', 'created_at', 'user')

# SURVEY PLAN MODEL
class SurveyPlan(models.Model):
  name = models.CharField(max_length=100)
  purpose = models.TextField()
  staffs = pgModels.ArrayField(models.CharField(max_length=50))
  output = pgModels.ArrayField(models.TextField())
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
# SURVEY PLAN ADMIN
@admin.register(SurveyPlan)
class SurveyPlanModel(ExportMixin, admin.ModelAdmin):
  search_fields = ('name',)
  list_display = ('name', 'staffs', 'created_at', 'user')

# SURVEY FORM MODEL
class SurveyForm(models.Model):
  PLATFORM_CHOICES = [
    ('Restorasi Mobile Apps', 'Restorasi Mobile Apps'),
    ('Konflik Web Apps', 'Konflik Web Apps'),
    ('E-sertifikasi Web Apps', 'E-sertifikasi Web Apps'),
  ]

  FORM_CHOICES = [
    ('Google Spreadsheets', 'Google Spreadsheets'),
    ('Google Forms', 'Google Forms'),
    ('Custom Forms', 'Custom Forms'),
  ]

  plan = models.OneToOneField(SurveyPlan, on_delete=models.CASCADE)
  platform_exists = models.BooleanField()
  platform_options = models.CharField(max_length=50, null=True, blank=True, choices=PLATFORM_CHOICES)
  form_type = models.CharField(max_length=50, null=True, blank=True, choices=FORM_CHOICES)
  form_variables = models.JSONField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

# SURVEY FORM ADMIN
@admin.register(SurveyForm)
class SurveyFormModel(ExportMixin, admin.ModelAdmin):
  search_fields = ('plan',)
  list_display = ('plan', 'platform_exists', 'created_at', 'user')

# 
class SurveySchedule(models.Model):
  STATUS_CHOICES = [
    ('progress', 'Progress'),
    ('complete', 'Complete'),
  ]

  form = models.OneToOneField(SurveyForm, on_delete=models.CASCADE)
  staffs = pgModels.ArrayField(models.CharField(max_length=50))
  start_date = models.DateField()
  end_date = models.DateField()
  status = models.CharField(max_length=20, choices=STATUS_CHOICES)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

# SURVEY FORM ADMIN
@admin.register(SurveySchedule)
class SurveyScheduleModel(ExportMixin, admin.ModelAdmin):
  search_fields = ('form',)
  list_display = ('form', 'staffs', 'created_at', 'user')