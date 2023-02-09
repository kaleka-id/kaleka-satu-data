from django import forms
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import path
from django.shortcuts import render, get_object_or_404
from operation.data_modification import geojsonData, geojsonDataObserver, addData, commentData, updateData, deleteData
from data.dataset.lahan import Lahan, LahanLegalitasLingkungan, LahanLegalitasSTDB
from leaflet.forms.widgets import LeafletWidget
from operation.signals import log_activity
from operation.ops_models.profiles import Profile

# 🚨DATASET LAHAN🚨
# Dictionary Lahan
@permission_required('data.search_lahan')
def lahan_dict(request):
  if request.method == 'GET':
    log_activity(request)

  q = ''
  page = ''

  if 'q' in request.GET:
    q = request.GET['q']
    data = Lahan.objects.filter(petani__nama_lengkap__icontains=q)
    p = Paginator(data, 20)
    page = request.GET.get('page')
    data_page = p.get_page(page)
  else:
    data_page = Lahan.objects.none()

  return render(request, 'dictionary/lahan.html', {'dataset': data_page, 'query': q, 'page': page})

# View dari daftar lahan
@permission_required('data.view_lahan')
def lahanList(request):
  if request.method == 'GET':
    log_activity(request)

  num_page = 20
  
  query = ''
  page = ''

  if 'q' in request.GET:
    query = request.GET['q']
    data = Lahan.objects.filter(
      Q(user=request.user, nama_lengkap__icontains=query) |
      Q(user=request.user, nik__icontains=query))
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)
  
  else:
    data = Lahan.objects.filter(user=request.user)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)

  return render(request, 'forms/lists/lahan.html', {'dataset': data_page, 'page': page, 'query': query})

# View dari daftar lahan dengan observer mode
@permission_required('data.view_lahan')
def lahanListObserver(request):
  if request.method == 'GET':
    log_activity(request)

  num_page = 20
  
  query = ''
  page = ''
  profile = Profile.objects.filter(user=request.user).values_list('user_observed', flat=True)

  if 'q' in request.GET:
    query = request.GET['q']
    data = Lahan.objects.filter(
      Q(user__in=profile, nama_lengkap__icontains=query) |
      Q(user__in=profile, nik__icontains=query))
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)
  
  else:
    data = Lahan.objects.filter(user__in=profile)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)

  return render(request, 'forms/lists/lahan_observer.html', {'dataset': data_page, 'page': page, 'query': query})

def lahanJSON(request):
  if request.method == 'GET':
    log_activity(request)
  return geojsonData(request, Lahan)

def lahanJSONObserver(request):
  if request.method == 'GET':
    log_activity(request)
  return geojsonDataObserver(request, Lahan)

# View dari informasi detil orang
@permission_required('data.view_orang')
def lahanDetail(request, pk):
  if request.method == 'GET':
    log_activity(request)
  
  lahan = get_object_or_404(Lahan, id=pk)
  dokling = LahanLegalitasLingkungan.objects.filter(legalitas_lahan=lahan.legalitas)
  stdb = LahanLegalitasSTDB.objects.filter(legalitas_lahan=lahan.legalitas)
  return render(request, 'forms/details/lahan.html', {
    'lahan': lahan,
    'dokling': dokling,
    'stdb': stdb,
  })

class lahanForm(forms.ModelForm):
  class Meta:
    model = Lahan
    fields = ('poligon_lahan', 'petani', 'legalitas', 'status_data')
    widgets = {
      # 'geom': LeafletWidget(),
      'poligon_lahan': forms.TextInput(),
      'petani': forms.TextInput(),
      'legalitas': forms.TextInput(),
    }

class lahanFormComment(forms.ModelForm):
  class Meta:
    model = Lahan
    fields = ('status_data', 'keterangan', 'user')

# View dari form penambahan lahan
@permission_required('data.add_lahan')
def lahan_form_add(request):
  if request.method == 'GET':
    log_activity(request)
  return addData(request, lahanForm, 'lahan_list', 'forms/form/lahan_add.html', 'data_lahan')

# View dari form perubahan lahan
@permission_required('data.change_lahan')
def lahan_form_update(request, pk):
  if request.method == 'GET':
    log_activity(request)
  return updateData(request, Lahan, pk, lahanForm, 'lahan_list', 'forms/form/lahan_update.html', 'data_lahan')

# View dari form perubahan lahan
@permission_required('data.change_lahan')
def lahan_form_comment(request, pk):
  if request.method == 'GET':
    log_activity(request)
  return commentData(request, Lahan, pk, lahanFormComment, 'lahan_list', 'forms/form/lahan_update.html', 'data_lahan')

# View untuk menghapus lahan
@permission_required('data.delete_testing')
def lahan_form_delete(request, pk):
  if request.method == 'GET':
    log_activity(request)
  return deleteData(request, Lahan, pk, 'lahan_list', 'data_lahan')

# 🚨DATASET LEGALITAS LAHAN🚨

urlpatterns = [
  path('dict/lahan/', lahan_dict, name='lahan_dict'),
  path('forms/lahan/', lahanList, name='lahan_list'),
  path('forms/lahan/observer/', lahanListObserver, name='lahan_list_observer'),
  path('forms/lahan-json/', lahanJSON, name='lahan_json'),
  path('forms/lahan-json/observer', lahanJSONObserver, name='lahan_json_observer'),
  path('forms/lahan/<uuid:pk>/', lahanDetail, name='lahan_detail'),
  path('forms/lahan-add/', lahan_form_add, name='lahan_form_add'),
  path('forms/lahan-update/<uuid:pk>/', lahan_form_update, name='lahan_form_update'),
  path('forms/lahan-comment/<uuid:pk>/', lahan_form_comment, name='lahan_form_comment'),
  path('forms/lahan-delete/<uuid:pk>/', lahan_form_delete, name='lahan_form_delete'),
]