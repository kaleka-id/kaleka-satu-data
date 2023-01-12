from django import forms
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import path
from django.shortcuts import render
from operation.data_modification import detailData, addData, updateData, deleteData
from data.dataset.orang import Orang

# DICTIONARY
@permission_required('data.search_orang')
def orang_dict(request):
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


# View dari informasi detil orang
@permission_required('data.view_orang')
def orangDetail(request, pk):
  return detailData(request, Orang, pk, 'forms/details/orang.html', 'orang')

# Form untuk menambahkan dan mengubah orang
class orangForm(forms.ModelForm):
  class Meta:
    model = Orang
    fields = ('nik', 'nama_lengkap', 'tempat_lahir', 'tanggal_lahir', 'status_kawin', 'profesi', 'rt', 'rw', 'alamat')
    widgets = {
      'tanggal_lahir': forms.DateInput(attrs={'type': 'date'}),
      'alamat': forms.TextInput(),
    }

# View dari form penambahan orang
@permission_required('data.add_orang')
def orang_form_add(request):
  return addData(request, orangForm, 'orang_list', 'forms/form/orang_add.html')

# View dari form perubahan orang
@permission_required('data.change_testing')
def orang_form_update(request, pk):
  return updateData(request, Orang, pk, orangForm, 'orang_list', 'forms/form/orang_update.html')

# View untuk menghapus orang
@permission_required('data.delete_testing')
def orang_form_delete(request, pk):
  return deleteData(request, Orang, pk, 'orang_list')

urlpatterns = [
  path('dict/orang/', orang_dict, name='orang_dict'),
  path('forms/orang/', orangList, name='orang_list'),
  path('forms/orang/<uuid:pk>/', orangDetail, name='orang_detail'),
  path('forms/orang-add/', orang_form_add, name='orang_form_add'),
  path('forms/orang-update/<uuid:pk>/', orang_form_update, name='orang_form_update'),
  path('forms/orang-delete/<uuid:pk>/', orang_form_delete, name='orang_form_delete'),
]