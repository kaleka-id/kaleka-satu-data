from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from operation.ops_models.webentry import WebEntry

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
  # LOGIKA UNTUK JENIS ELEKTRONIK
  if request.user_agent.is_mobile:
    electronic = 'Smartphone'
  elif request.user_agent.is_tablet:
    electronic = 'Tablet'
  elif request.user_agent.is_pc:
    electronic = 'PC/Laptop'
  else:
    electronic = None

  # LOGIKA UNTUK TIPE DEVICE
  if request.user_agent.device.family == None:
    device_type = 'None'
  else:
    device_type=request.user_agent.device.family

  # LOGIKA UNTUK BRAND DEVICE 
  if request.user_agent.device.brand == None:
    device_brand = 'None'
  else:
    device_brand=request.user_agent.device.brand

  # LOGIKA UNITUK MODEL DEVICE
  if request.user_agent.device.model == None:
    device_model = 'None'
  else:
    device_model=request.user_agent.device.model

  WebEntry.objects.create(
    action='User Login', 
    ip=request.META.get('REMOTE_ADDR'),
    electronic=electronic,
    is_touchscreen=request.user_agent.is_touch_capable,
    is_bot=request.user_agent.is_bot,
    os_type=request.user_agent.os.family,
    os_version=request.user_agent.os.version_string,
    browser_type=request.user_agent.browser.family,
    browser_version=request.user_agent.browser.version_string,
    device_type=device_type,
    device_brand=device_brand,
    device_model=device_model,
    username=user.username)

@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
  creds = credentials
  
  # LOGIKA UNTUK JENIS ELEKTRONIK
  if request.user_agent.is_mobile:
    electronic = 'Smartphone'
  elif request.user_agent.is_tablet:
    electronic = 'Tablet'
  elif request.user_agent.is_pc:
    electronic = 'PC/Laptop'
  else:
    electronic = None

  # LOGIKA UNTUK TIPE DEVICE
  if request.user_agent.device.family == None:
    device_type = 'None'
  else:
    device_type=request.user_agent.device.family

  # LOGIKA UNTUK BRAND DEVICE 
  if request.user_agent.device.brand == None:
    device_brand = 'None'
  else:
    device_brand=request.user_agent.device.brand

  # LOGIKA UNITUK MODEL DEVICE
  if request.user_agent.device.model == None:
    device_model = 'None'
  else:
    device_model=request.user_agent.device.model

  WebEntry.objects.create(
    action='User Login Failed', 
    ip=request.META.get('REMOTE_ADDR'),
    electronic=electronic,
    is_touchscreen=request.user_agent.is_touch_capable,
    is_bot=request.user_agent.is_bot,
    os_type=request.user_agent.os.family,
    os_version=request.user_agent.os.version_string,
    browser_type=request.user_agent.browser.family,
    browser_version=request.user_agent.browser.version_string,
    device_type=device_type,
    device_brand=device_brand,
    device_model=device_model,
    username=creds['username'])

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
  # LOGIKA UNTUK JENIS ELEKTRONIK
  if request.user_agent.is_mobile:
    electronic = 'Smartphone'
  elif request.user_agent.is_tablet:
    electronic = 'Tablet'
  elif request.user_agent.is_pc:
    electronic = 'PC/Laptop'
  else:
    electronic = None

  # LOGIKA UNTUK TIPE DEVICE
  if request.user_agent.device.family == None:
    device_type = 'None'
  else:
    device_type=request.user_agent.device.family

  # LOGIKA UNTUK BRAND DEVICE 
  if request.user_agent.device.brand == None:
    device_brand = 'None'
  else:
    device_brand=request.user_agent.device.brand

  # LOGIKA UNITUK MODEL DEVICE
  if request.user_agent.device.model == None:
    device_model = 'None'
  else:
    device_model=request.user_agent.device.model

  WebEntry.objects.create(
    action='User Logout', 
    ip=request.META.get('REMOTE_ADDR'),
    electronic=electronic,
    is_touchscreen=request.user_agent.is_touch_capable,
    is_bot=request.user_agent.is_bot,
    os_type=request.user_agent.os.family,
    os_version=request.user_agent.os.version_string,
    browser_type=request.user_agent.browser.family,
    browser_version=request.user_agent.browser.version_string,
    device_type=device_type,
    device_brand=device_brand,
    device_model=device_model,
    username=user.username)