from django import forms
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import path
from django.shortcuts import render
from operation.data_modification import detailData, addData, updateData, commentData, deleteData
from data.dataset.orang import Orang
from operation.signals import log_activity
from operation.ops_models.profiles import Profile

# DICTIONARY
@permission_required('data.search_orang')
def orang_dict(request):
  log_activity(request)

  q = None
  page = None

  if 'q' in request.GET:
    q = request.GET['q']
    data = Orang.objects.filter(
      Q(nama_lengkap__icontains=q) |
      Q(nik__icontains=q)).order_by('nama_lengkap')
    p = Paginator(data, 20)
    page = request.GET.get('page')
    data_page = p.get_page(page)
  else:
    data_page = Orang.objects.none()

  return render(request, 'dictionary/orang.html', {'dataset': data_page, 'query': q, 'page': page})

# FORM
# View dari daftar orang
@permission_required('data.view_orang')
def orangList(request):
  log_activity(request)

  num_page = 20
  
  query = None
  page = None

  if 'q' in request.GET:
    query = request.GET['q']
    data = Orang.objects.filter(
      Q(user=request.user, nama_lengkap__icontains=query) |
      Q(user=request.user, nik__icontains=query))
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)
  
  else:
    data = Orang.objects.filter(user=request.user)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)

  return render(request, 'forms/lists/orang.html', {'dataset': data_page, 'page': page, 'query': query})

# View dari daftar orang untuk observer
@permission_required('data.view_orang')
def orangListObserver(request):
  log_activity(request)

  num_page = 20
  
  query = ''
  page = ''
  profile = Profile.objects.filter(user=request.user).values_list('user_observed', flat=True)

  if 'q' in request.GET:
    query = request.GET['q']
    data = Orang.objects.filter(
      Q(user__in=profile, nama_lengkap__icontains=query) |
      Q(user__in=profile, nik__icontains=query))
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)
  
  else:
    data = Orang.objects.filter(user__in=profile)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)

  return render(request, 'forms/lists/orang_observer.html', {
    'dataset': data_page, 
    'page': page, 
    'query': query})


# View dari informasi detil orang
@permission_required('data.view_orang')
def orangDetail(request, pk):
  log_activity(request)

  return detailData(request, Orang, pk, 'forms/details/orang.html', 'orang')

# Form untuk menambahkan dan mengubah orang
class orangForm(forms.ModelForm):
  class Meta:
    model = Orang
    fields = ('nik', 'nama_lengkap', 'jenis_kelamin', 'tempat_lahir', 'tanggal_lahir', 'status_kawin', 'profesi', 'rt', 'rw', 'alamat', 'status_data', 'keterangan')
    widgets = {
      'tanggal_lahir': forms.DateInput(attrs={'type': 'date'}),
      'alamat': forms.TextInput(),
    }

# Form untuk komentar orang
class orangFormComment(forms.ModelForm):
  class Meta:
    model = Orang
    fields = ('status_data', 'keterangan', 'user')

# View dari form penambahan orang
@permission_required('data.add_orang')
def orang_form_add(request):
  log_activity(request)
  return addData(request, orangForm, 'orang_list', 'forms/form/orang_add.html', 'data_orang')

# View dari form perubahan orang
@permission_required('data.change_orang')
def orang_form_update(request, pk):
  log_activity(request)
  return updateData(request, Orang, pk, orangForm, 'orang_list', 'forms/form/orang_update.html', 'data_orang')

# View dari form komentar orang
@permission_required('data.change_orang')
def orang_form_comment(request, pk):
  log_activity(request)
  return commentData(request, Orang, pk, orangFormComment, 'orang_list', 'forms/form/orang_update.html', 'data_orang')

# View untuk menghapus orang
@permission_required('data.delete_orang')
def orang_form_delete(request, pk):
  log_activity(request)
  return deleteData(request, Orang, pk, 'orang_list', 'data_orang')

urlpatterns = [
  path('dict/orang/', orang_dict, name='orang_dict'),
  path('forms/orang/', orangList, name='orang_list'),
  path('forms/orang/observer/', orangListObserver, name='orang_list_observer'),
  path('forms/orang/<uuid:pk>/', orangDetail, name='orang_detail'),
  path('forms/orang-add/', orang_form_add, name='orang_form_add'),
  path('forms/orang-update/<uuid:pk>/', orang_form_update, name='orang_form_update'),
  path('forms/orang-comment/<uuid:pk>/', orang_form_comment, name='orang_form_comment'),
  path('forms/orang-delete/<uuid:pk>/', orang_form_delete, name='orang_form_delete'),
]