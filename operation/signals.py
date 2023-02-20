from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from operation.ops_models.web_entry import WebEntry
from operation.ops_models.activity_log import ActivityLog
import requests
import json
from satudata_project.settings import DEBUG

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
  if not DEBUG:
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
  if not DEBUG:
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
  if not DEBUG:
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

# LOGGING AKTIVITAS
def log_activity(request):
  if not DEBUG:
    # FETCH DATA GEOIP
    ip = request.META.get('REMOTE_ADDR')
    res = requests.get(f'http://ip-api.com/json/{ip}').text
    geoip = json.loads(res)
    
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

    # LOGIKA UNTUK USERNAME
    if request.user.is_authenticated:
      username = request.user.username
    else:
      username = 'User not login'

    activity = ActivityLog.objects.create(
      url_access=request.build_absolute_uri(), 
      ip=ip,
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
      username=username,
      country_code=geoip['countryCode'],
      country=geoip['country'],
      region_code=geoip['region'],
      region=geoip['regionName'],
      city=geoip['city'],
      lat=geoip['lat'],
      lon=geoip['lon'],
      timezone=geoip['timezone'],
      isp=geoip['isp'],
      isp_detail=geoip['as'])

    return activity