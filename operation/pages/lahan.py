from django import forms
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import path
from django.shortcuts import render
from operation.data_modification import geojsonData, detailData, addData, updateData, deleteData
from data.dataset.lahan import Lahan
from leaflet.forms.widgets import LeafletWidget
from operation.signals import log_activity

# DICTIONARY
@permission_required('data.search_lahan')
def lahan_dict(request):
  log_activity(request)

  q = None
  page = None

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
  log_activity(request)

  num_page = 20
  
  query = None
  page = None

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

def lahanJSON(request):
  log_activity(request)
  return geojsonData(request, Lahan)

# View dari informasi detil orang
@permission_required('data.view_orang')
def lahanDetail(request, pk):
  log_activity(request)
  return detailData(request, Lahan, pk, 'forms/details/lahan.html', 'lahan')

class lahanForm(forms.ModelForm):
  class Meta:
    model = Lahan
    fields = ('geom', 'petani', 'status_petani', 'jenis_legalitas', 'nomor_legalitas', 'tahun_legalitas')
    widgets = {
      'geom': LeafletWidget(),
      'petani': forms.TextInput(),
    }

# View dari form penambahan lahan
@permission_required('data.add_lahan')
def lahan_form_add(request):
  log_activity(request)
  return addData(request, lahanForm, 'lahan_list', 'forms/form/lahan_add.html', 'data_lahan')

# View dari form perubahan lahan
@permission_required('data.change_lahan')
def lahan_form_update(request, pk):
  log_activity(request)
  return updateData(request, Lahan, pk, lahanForm, 'lahan_list', 'forms/form/lahan_update.html', 'data_lahan')

# View untuk menghapus lahan
@permission_required('data.delete_testing')
def lahan_form_delete(request, pk):
  log_activity(request)
  return deleteData(request, Lahan, pk, 'lahan_list', 'data_lahan')

urlpatterns = [
  path('dict/lahan/', lahan_dict, name='lahan_dict'),
  path('forms/lahan/', lahanList, name='lahan_list'),
  path('forms/lahan-json/', lahanJSON, name='lahan_json'),
  path('forms/lahan/<uuid:pk>/', lahanDetail, name='lahan_detail'),
  path('forms/lahan-add/', lahan_form_add, name='lahan_form_add'),
  path('forms/lahan-update/<uuid:pk>/', lahan_form_update, name='lahan_form_update'),
  path('forms/lahan-delete/<uuid:pk>/', lahan_form_delete, name='lahan_form_delete'),
]