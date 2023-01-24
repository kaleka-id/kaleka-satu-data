from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from operation.ops_models.webentry import WebEntry

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
  WebEntry.objects.create(
    action='User Login', 
    ip=request.META.get('REMOTE_ADDR'),
    username=user.username)

@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
  creds = credentials
  WebEntry.objects.create(
    action='User Login Failed', 
    ip=request.META.get('REMOTE_ADDR'),
    username=creds['username'])

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
  WebEntry.objects.create(
    action='User Logout', 
    ip=request.META.get('REMOTE_ADDR'),
    username=user.username)

