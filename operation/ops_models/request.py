from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

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
class RequestModel(admin.ModelAdmin):
  search_fields = ('subject',)
  list_display = ('subject', 'request_type', 'status', 'created_at', 'user')