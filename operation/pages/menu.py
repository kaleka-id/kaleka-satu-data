from django import forms as iforms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path
from django.core.mail import EmailMessage
from operation.models import Forms, Docs, Dictionary, Dashboard, Catalog, Profile, Request
from operation.data_modification import detailData, addData, updateData
from operation.signals import log_activity
from operation.ops_models.data_logs import DataLog

def home(request):
  log_activity(request)
  return render(request, 'menu/home.html')

@permission_required('operation.view_forms')
def forms(request):
  log_activity(request)
  desc = Forms.objects.all().order_by('nama')
  return render(request, 'menu/forms.html', {
    'forms': desc
  })

@permission_required('operation.view_docs')
def docs(request):
  log_activity(request)
  desc = Docs.objects.all().order_by('judul')
  return render(request, 'menu/docs.html', {
    'docs': desc
  })

@permission_required('operation.view_docs')
def docs_detail(request, pk):
  log_activity(request)
  return detailData(request, Docs, pk, 'menu/docs_detail.html', 'docs')

@permission_required('operation.view_docs')
def dictionary(request):
  log_activity(request)
  desc = Dictionary.objects.all().order_by('nama')
  return render(request, 'menu/dictionary.html', {
    'dict': desc
  })

@login_required
def dashboard(request):
  log_activity(request)
  desc = Dashboard.objects.all().order_by('nama')
  return render(request, 'menu/dashboard.html', {
    'dashboard': desc
  })

@login_required
def dashboard_detail(request, pk):
  log_activity(request)
  return detailData(request, Dashboard, pk, 'menu/dashboard_detail.html', 'dashboard')

@login_required
def catalog(request):
  log_activity(request)
  desc = Catalog.objects.all().order_by('nama')
  return render(request, 'menu/catalog.html', {
    'catalog': desc
  })

@login_required
def catalog_detail(request, pk):
  log_activity(request)
  return detailData(request, Catalog, pk, 'menu/catalog_detail.html', 'catalog')

@login_required
def profile(request):
  log_activity(request)
  return render(request, 'menu/profile.html')

class ProfileForm(iforms.ModelForm):
  class Meta:
    model = Profile
    fields = ('avatar',)

@login_required
def profile_form_add(request):
  log_activity(request)
  return addData(request, ProfileForm, 'profile', 'menu/profile_add.html', 'operation_profile')

@login_required
def profile_form_update(request, pk):
  log_activity(request)
  return updateData(request, Profile, pk, ProfileForm, 'profile', 'menu/profile_update.html', 'operation_profile')

@login_required
def about(request):
  log_activity(request)
  return render(request, 'menu/about.html')

def tutorial(request):
  log_activity(request)
  return render(request, 'menu/tutorial.html')

def request(request):
  dataset = Request.objects.filter(user=request.user)
  log_activity(request)
  return render(request, 'menu/request.html', {'dataset': dataset})

# Form untuk menambahkan request
class requestForm(iforms.ModelForm):
  class Meta:
    model = Request
    fields = ('subject', 'request_type', 'message')

@login_required
def request_form_add(request):
  # LOGIKA UNTUK TIPE DEVICE
  if request.user_agent.device.family == None:
    device_type = 'None'
  else:
    device_type=request.user_agent.device.family

  # KIRIM KE DATABASE
  if request.method == 'POST':
    form = requestForm(request.POST, request.FILES)
    if form.is_valid():
      item = form.save(commit= False)
      item.user = request.user
      item.save()
      form.save_m2m()

      log_activity(request)

      DataLog.objects.create(
        action='INSERT',
        dataset='operation_request',
        id_dataset=item.id,
        user=request.user,
        ip_user=request.META.get('REMOTE_ADDR'),
        device_user=device_type,
        os_user=request.user_agent.os.family,
        browser_user=request.user_agent.browser.family)

      email = EmailMessage(
        item.subject,
        item.message,
        'satudata@kaleka.id',
        to=[request.user.email],
        cc=['cwiratama@kaleka.id', 'afaiz@kaleka.id', 'riwanda@kaleka.id'],
        headers={'Message-ID': item.id},
      )
      email.send()

      return redirect('request')
  
  else:
    form = requestForm()

  return render(request, 'menu/request_add.html', {
    'form': form 
  })

@login_required
def tutorial_geoserver_qgis(request):
  log_activity(request)
  return render(request, 'menu/tutorial/geoserver_qgis.html')

urlpatterns = [
  path('', home, name='home'),
  path('forms/', forms, name='forms'),
  path('docs/', docs, name='docs'),
  path('docs/<int:pk>/', docs_detail, name='docs_detail'),
  path('dict/', dictionary, name='dictionary'),
  path('dashboard/', dashboard, name='dashboard'),
  path('dashboard/<int:pk>/', dashboard_detail, name='dashboard_detail'),
  path('catalog/', catalog, name='catalog'),
  path('catalog/<int:pk>/', catalog_detail, name='catalog_detail'),
  path('profile/', profile, name='profile'),
  path('profile/add/', profile_form_add, name='profile_form_add'),
  path('profile/<uuid:pk>/', profile_form_update, name='profile_form_update'),
  path('about/', about, name='about'),
  path('tutorial/', tutorial, name='tutorial'),
  path('request/', request, name='request'),
  path('request/add/', request_form_add, name='request_form_add'),
  path('tutorial/tutorial-geoserver-di-qgis', tutorial_geoserver_qgis, name='tutorial_geoserver_qgis'),
]