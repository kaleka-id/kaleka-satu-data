from django import forms
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.urls import path
from django.shortcuts import render, get_object_or_404
from operation.data_modification import geojsonData, detailData, addData, updateData, deleteData
from data.dataset.kegiatan import Kegiatan, PesertaKegiatan, FotoKegiatan

# 🚨KEGIATAN🚨
@permission_required('data.search_kegiatan')
def kegiatan_dict(request):
  q = None
  page = None

  if 'q' in request.GET:
    q = request.GET['q']
    data = Kegiatan.objects.filter(nama__icontains=q)
    p = Paginator(data, 20)
    page = request.GET.get('page')
    data_page = p.get_page(page)
  else:
    data_page = Kegiatan.objects.none()

  return render(request, 'dictionary/kegiatan.html', {
    'dataset': data_page, 'query': q, 'page': page})

# View dari daftar kegiatan
@permission_required('data.view_kegiatan')
def kegiatanList(request):
  num_page = 20
  
  query = None
  page = None

  if 'q' in request.GET:
    query = request.GET['q']
    data = Kegiatan.objects.filter(nama__icontains=query, user=request.user)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)
  
  else:
    data = Kegiatan.objects.filter(user=request.user)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)

  return render(request, 'forms/lists/kegiatan.html', {'dataset': data_page, 'page': page, 'query': query})

# View dari informasi detil kegiatan
@permission_required('data.view_kegiatan')
def kegiatanDetail(request, pk):
  kegiatan = get_object_or_404(Kegiatan, id=pk)
  peserta = PesertaKegiatan.objects.filter(kegiatan=pk)
  foto = FotoKegiatan.objects.filter(kegiatan=pk)
  return render(request, 'forms/details/kegiatan.html', {
    'kegiatan': kegiatan, 
    'peserta': peserta,
    'foto': foto})

# Form untuk menambahkan dan mengubah kegiatan
class kegiatanForm(forms.ModelForm):
  class Meta:
    model = Kegiatan
    fields = ('nama', 'tanggal_mulai', 'tanggal_selesai')
    widgets = {
      'tanggal_mulai': forms.DateInput(attrs={'type': 'date'}),
      'tanggal_selesai': forms.DateInput(attrs={'type': 'date'}),
    }

# View dari form penambahan kegiatan
@permission_required('data.add_kegiatan')
def kegiatan_form_add(request):
  return addData(request, kegiatanForm, 'kegiatan_list', 'forms/form/kegiatan_add.html')

# View dari form perubahan kegiatan
@permission_required('data.change_kegiatan')
def kegiatan_form_update(request, pk):
  return updateData(request, Kegiatan, pk, kegiatanForm, 'kegiatan_list', 'forms/form/kegiatan_update.html')

# View untuk menghapus peserta kegiatan
@permission_required('data.delete_kegiatan')
def kegiatan_form_delete(request, pk):
  return deleteData(request, Kegiatan, pk, 'kegiatan_list')

# 🚨PESERTA KEGIATAN🚨
# View dari daftar foto kegiatan
@permission_required('data.view_peserta_kegiatan')
def pesertaKegiatanList(request):
  num_page = 20
  
  query = None
  page = None

  if 'q' in request.GET:
    query = request.GET['q']
    data = PesertaKegiatan.objects.filter(peserta__nama_lengkap__icontains=query, user=request.user)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)
  
  else:
    data = PesertaKegiatan.objects.filter(user=request.user)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)

  return render(request, 'forms/lists/kegiatan_peserta.html', {'dataset': data_page, 'page': page, 'query': query})

# Form untuk menambahkan dan mengubah peserta kegiatan
class pesertaKegiatanForm(forms.ModelForm):
  class Meta:
    model = PesertaKegiatan
    fields = ('kegiatan', 'peserta', 'status_kehadiran')
    widgets = {
      'kegiatan': forms.TextInput(),
      'peserta': forms.TextInput(),
    }

# View dari form penambahan peserta kegiatan
@permission_required('data.add_peserta_kegiatan')
def peserta_kegiatan_form_add(request):
  return addData(request, pesertaKegiatanForm, 'peserta_kegiatan_list', 'forms/form/kegiatan_peserta_add.html')

# View dari form perubahan peserta kegiatan
@permission_required('data.change_peserta_kegiatan')
def peserta_kegiatan_form_update(request, pk):
  return updateData(request, PesertaKegiatan, pk, pesertaKegiatanForm, 'peserta_kegiatan_list', 'forms/form/kegiatan_peserta_update.html')

# View untuk menghapus peserta kegiatan
@permission_required('data.delete_peserta_kegiatan')
def peserta_kegiatan_form_delete(request, pk):
  return deleteData(request, PesertaKegiatan, pk, 'peserta_kegiatan_list')

# 🚨FOTO KEGIATAN🚨
# View dari daftar foto kegiatan
@permission_required('data.view_foto_kegiatan')
def fotoKegiatanList(request):
  num_page = 20
  
  query = None
  page = None

  if 'q' in request.GET:
    query = request.GET['q']
    data = FotoKegiatan.objects.filter(kegiatan__nama__icontains=query, user=request.user)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)
  
  else:
    data = FotoKegiatan.objects.filter(user=request.user)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)

  return render(request, 'forms/lists/kegiatan_foto.html', {'dataset': data_page, 'page': page, 'query': query})

# Form untuk menambahkan dan mengubah foto kegiatan
class fotoKegiatanForm(forms.ModelForm):
  class Meta:
    model = FotoKegiatan
    fields = ('kegiatan', 'foto')
    widgets = {
      'kegiatan': forms.TextInput(),
    }

# View dari form penambahan foto kegiatan
@permission_required('data.add_foto_kegiatan')
def foto_kegiatan_form_add(request):
  return addData(request, fotoKegiatanForm, 'foto_kegiatan_list', 'forms/form/kegiatan_foto_add.html')

# View dari form perubahan foto kegiatan
@permission_required('data.change_foto_kegiatan')
def foto_kegiatan_form_update(request, pk):
  return updateData(request, FotoKegiatan, pk, fotoKegiatanForm, 'foto_kegiatan_list', 'forms/form/kegiatan_foto_update.html')

# View untuk menghapus foto kegiatan
@permission_required('data.delete_foto_kegiatan')
def foto_kegiatan_form_delete(request, pk):
  return deleteData(request, FotoKegiatan, pk, 'foto_kegiatan_list')

urlpatterns = [
  path('dict/kegiatan/', kegiatan_dict, name='kegiatan_dict'),
  path('forms/kegiatan/', kegiatanList, name='kegiatan_list'),
  path('forms/kegiatan/<uuid:pk>/', kegiatanDetail, name='kegiatan_detail'),
  path('forms/kegiatan-add/', kegiatan_form_add, name='kegiatan_form_add'),
  path('forms/kegiatan-update/<uuid:pk>/', kegiatan_form_update, name='kegiatan_form_update'),
  path('forms/kegiatan-delete/<uuid:pk>/', kegiatan_form_delete, name='kegiatan_form_delete'),

  path('forms/kegiatan/peserta', pesertaKegiatanList, name='peserta_kegiatan_list'),
  path('forms/kegiatan/peserta-add/', peserta_kegiatan_form_add, name='peserta_kegiatan_form_add'),
  path('forms/kegiatan/peserta-update/<uuid:pk>/', peserta_kegiatan_form_update, name='peserta_kegiatan_form_update'),
  path('forms/kegiatan/peserta-delete/<uuid:pk>/', peserta_kegiatan_form_delete, name='peserta_kegiatan_form_delete'),

  path('forms/kegiatan/foto', fotoKegiatanList, name='foto_kegiatan_list'),
  path('forms/kegiatan/foto-add/', foto_kegiatan_form_add, name='foto_kegiatan_form_add'),
  path('forms/kegiatan/foto-update/<uuid:pk>/', foto_kegiatan_form_update, name='foto_kegiatan_form_update'),
  path('forms/kegiatan/foto-delete/<uuid:pk>/', foto_kegiatan_form_delete, name='foto_kegiatan_form_delete'),
]