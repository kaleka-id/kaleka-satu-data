from django.shortcuts import render, redirect, get_object_or_404
from django.core.serializers import serialize
from django.http import HttpResponse
from operation.ops_models.data_logs import DataLog
from operation.ops_models.profiles import Profile
from django.contrib.auth.models import User
import requests
import json
from satudata_project.settings import DEBUG

# LIST OF DATA MODIFICATION FUNCTIONS 
def geojsonData(request, dataset):
  place = serialize('geojson', dataset.objects.filter(user=request.user))
  return HttpResponse(place, content_type='json')

def geojsonDataObserver(request, dataset):
  profile = Profile.objects.filter(user=request.user).values_list('user_observed', flat=True)
  place = serialize('geojson', dataset.objects.filter(user__in=profile))
  return HttpResponse(place, content_type='json')

def detailData(request, dataset, pk, url, callback):
  desc = get_object_or_404(dataset, id=pk)
  return render(request, url, {callback: desc})

def addData(request, forms, redirects, url, db_dataset):
  if not DEBUG:
    # FETCH DATA GEOIP
    ip = request.META.get('REMOTE_ADDR')
    res = requests.get(f'http://ip-api.com/json/{ip}').text
    geoip = json.loads(res)

    # LOGIKA UNTUK TIPE DEVICE
    if request.user_agent.device.family == None:
      device_type = 'None'
    else:
      device_type=request.user_agent.device.family

  # KIRIM KE DATABASE
  if request.method == 'POST':
    form = forms(request.POST, request.FILES)
    if form.is_valid():
      item = form.save(commit= False)
      item.user = request.user
      item.save()
      form.save_m2m()
      if not DEBUG:
        DataLog.objects.create(
          action='INSERT',
          dataset=db_dataset,
          id_dataset=item.id,
          user=request.user,
          ip_user=request.META.get('REMOTE_ADDR'),
          device_user=device_type,
          os_user=request.user_agent.os.family,
          browser_user=request.user_agent.browser.family,
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
      return redirect(redirects)
  
  else:
    form = forms()

  return render(request, url, {
    'form': form 
  })

def updateData(request, dataset, pk, forms, redirects, url, db_dataset):
  if not DEBUG:
    # FETCH DATA GEOIP
    ip = request.META.get('REMOTE_ADDR')
    res = requests.get(f'http://ip-api.com/json/{ip}').text
    geoip = json.loads(res)

    # LOGIKA UNTUK TIPE DEVICE
    if request.user_agent.device.family == None:
      device_type = 'None'
    else:
      device_type=request.user_agent.device.family

  item = get_object_or_404(dataset, id=pk)
  form = forms(request.POST or None, request.FILES or None, instance=item)
  data = dataset.objects.filter(user=request.user)
  
  if request.method == 'POST':
    if form.is_valid():
      item.user = request.user
      form.save()
      if not DEBUG:
        DataLog.objects.create(
          action='UPDATE',
          dataset=db_dataset,
          id_dataset=item.id,
          user=request.user,
          ip_user=request.META.get('REMOTE_ADDR'),
          device_user=device_type,
          os_user=request.user_agent.os.family,
          browser_user=request.user_agent.browser.family,
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
      return redirect(redirects)

  return render(request, url, {'form':form, 'data':data})

def commentData(request, dataset, pk, forms, redirects, url, db_dataset):
  if not DEBUG:
    # FETCH DATA GEOIP
    ip = request.META.get('REMOTE_ADDR')
    res = requests.get(f'http://ip-api.com/json/{ip}').text
    geoip = json.loads(res)

    # LOGIKA UNTUK TIPE DEVICE
    if request.user_agent.device.family == None:
      device_type = 'None'
    else:
      device_type=request.user_agent.device.family

  item = get_object_or_404(dataset, id=pk)
  form = forms(request.POST or None, request.FILES or None, instance=item)
  data = dataset.objects.filter(user=request.user)
  
  form.fields["user"].queryset = User.objects.filter(id__in=Profile.objects.filter(user=request.user).values_list('user_observed', flat=True))

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      if not DEBUG:
        DataLog.objects.create(
          action='UPDATE',
          dataset=db_dataset,
          id_dataset=item.id,
          user=request.user,
          ip_user=request.META.get('REMOTE_ADDR'),
          device_user=device_type,
          os_user=request.user_agent.os.family,
          browser_user=request.user_agent.browser.family,
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
      return redirect(redirects)

  return render(request, url, {'form':form, 'data':data})

def deleteData(request, dataset, pk, redirects, db_dataset):
  if not DEBUG:
    # FETCH DATA GEOIP
    ip = request.META.get('REMOTE_ADDR')
    res = requests.get(f'http://ip-api.com/json/{ip}').text
    geoip = json.loads(res)

    # LOGIKA UNTUK TIPE DEVICE
    if request.user_agent.device.family == None:
      device_type = 'None'
    else:
      device_type=request.user_agent.device.family

  item = get_object_or_404(dataset, id=pk)

  if request.method == 'GET':
    print('deleted function')
    print(item)
    if not DEBUG:
      DataLog.objects.create(
        action='DELETE',
        dataset=db_dataset,
        id_dataset=item.id,
        user=request.user,
        ip_user=request.META.get('REMOTE_ADDR'),
        device_user=device_type,
        os_user=request.user_agent.os.family,
        browser_user=request.user_agent.browser.family,
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
    item.delete()
  return redirect(redirects)