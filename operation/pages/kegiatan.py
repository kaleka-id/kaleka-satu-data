from django import forms
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.urls import path
from django.shortcuts import render, redirect, get_object_or_404
from operation.data_modification import geojsonData, detailData, addData, updateData, commentData, deleteData
from data.dataset.kegiatan import Kegiatan, PesertaKegiatan, FotoKegiatan
from operation.ops_models.data_logs import DataLog
from operation.signals import log_activity
from operation.ops_models.profiles import Profile

# 🚨KEGIATAN🚨
@permission_required('data.search_kegiatan')
def kegiatan_dict(request):
  if request.method == 'GET':
    log_activity(request)

  q = ''
  page = ''

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
  if request.method == 'GET':
    log_activity(request)

  num_page = 20
  
  query = ''
  page = ''

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

# View dari daftar kegiatan mode observer
@permission_required('data.view_kegiatan')
def kegiatanListObserver(request):
  if request.method == 'GET':
    log_activity(request)

  num_page = 20
  
  query = ''
  page = ''
  profile = Profile.objects.filter(user=request.user).values_list('user_observed', flat=True)

  if 'q' in request.GET:
    query = request.GET['q']
    data = Kegiatan.objects.filter(nama__icontains=query, user__in=profile)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)
  
  else:
    data = Kegiatan.objects.filter(user__in=profile)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)

  return render(request, 'forms/lists/kegiatan_observer.html', {'dataset': data_page, 'page': page, 'query': query})

# View dari informasi detil kegiatan
@permission_required('data.view_kegiatan')
def kegiatanDetail(request, pk):
  if request.method == 'GET':
    log_activity(request)

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
    fields = ('nama', 'tanggal_mulai', 'tanggal_selesai', 'status_data', 'keterangan')
    widgets = {
      'tanggal_mulai': forms.DateInput(attrs={'type': 'date'}),
      'tanggal_selesai': forms.DateInput(attrs={'type': 'date'}),
    }

# Form untuk komentar kegiatan
class kegiatanFormComment(forms.ModelForm):
  class Meta:
    model = Kegiatan
    fields = ('status_data', 'keterangan', 'user')

# View dari form penambahan kegiatan
@permission_required('data.add_kegiatan')
def kegiatan_form_add(request):
  if request.method == 'GET':
    log_activity(request)
  return addData(request, kegiatanForm, 'kegiatan_list', 'forms/form/kegiatan_add.html', 'data_kegiatan')

# View dari form perubahan kegiatan
@permission_required('data.change_kegiatan')
def kegiatan_form_update(request, pk):
  if request.method == 'GET':
    log_activity(request)
  return updateData(request, Kegiatan, pk, kegiatanForm, 'kegiatan_list', 'forms/form/kegiatan_update.html', 'data_kegiatan')

# View dari form perubahan kegiatan
@permission_required('data.change_kegiatan')
def kegiatan_form_comment(request, pk):
  if request.method == 'GET':
    log_activity(request)
  return commentData(request, Kegiatan, pk, kegiatanFormComment, 'kegiatan_list', 'forms/form/kegiatan_update.html', 'data_kegiatan')

# View untuk menghapus peserta kegiatan
@permission_required('data.delete_kegiatan')
def kegiatan_form_delete(request, pk):
  if request.method == 'GET':
    log_activity(request)
  return deleteData(request, Kegiatan, pk, 'kegiatan_list', 'data_kegiatan')

# 🚨PESERTA KEGIATAN🚨
# View dari daftar foto kegiatan
@permission_required('data.view_pesertakegiatan')
def pesertaKegiatanList(request):
  if request.method == 'GET':
    log_activity(request)

  num_page = 20
  
  query = ''
  page = ''

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

# View dari daftar foto kegiatan
@permission_required('data.view_pesertakegiatan')
def pesertaKegiatanListObserver(request):
  if request.method == 'GET':
    log_activity(request)

  num_page = 20
  
  query = ''
  page = ''
  profile = Profile.objects.filter(user=request.user).values_list('user_observed', flat=True)

  if 'q' in request.GET:
    query = request.GET['q']
    data = PesertaKegiatan.objects.filter(peserta__nama_lengkap__icontains=query, user__in=profile)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)
  
  else:
    data = PesertaKegiatan.objects.filter(user__in=profile)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)

  return render(request, 'forms/lists/kegiatan_peserta_observer.html', {'dataset': data_page, 'page': page, 'query': query})

# Form untuk menambahkan dan mengubah peserta kegiatan
class pesertaKegiatanForm(forms.ModelForm):
  class Meta:
    model = PesertaKegiatan
    fields = ('kegiatan', 'peserta', 'status_kehadiran')
    widgets = {
      'kegiatan': forms.TextInput(),
      'peserta': forms.TextInput(),
    }

# Form untuk komentar peserta kegiatan
class pesertaKegiatanFormComment(forms.ModelForm):
  class Meta:
    model = PesertaKegiatan
    fields = ('user',)

# View dari form penambahan peserta kegiatan
@permission_required('data.add_pesertakegiatan')
def peserta_kegiatan_form_add(request):
  if request.method == 'GET':
    log_activity(request)
  return addData(request, pesertaKegiatanForm, 'peserta_kegiatan_list', 'forms/form/kegiatan_peserta_add.html', 'data_pesertakegiatan')

# View dari form perubahan peserta kegiatan
@permission_required('data.change_pesertakegiatan')
def peserta_kegiatan_form_update(request, pk):
  if request.method == 'GET':
    log_activity(request)
  return updateData(request, PesertaKegiatan, pk, pesertaKegiatanForm, 'peserta_kegiatan_list', 'forms/form/kegiatan_peserta_update.html', 'data_pesertakegiatan')

# View dari form komentar peserta kegiatan
@permission_required('data.change_pesertakegiatan')
def peserta_kegiatan_form_comment(request, pk):
  if request.method == 'GET':
    log_activity(request)
  return commentData(request, PesertaKegiatan, pk, pesertaKegiatanFormComment, 'peserta_kegiatan_list', 'forms/form/kegiatan_peserta_update.html', 'data_pesertakegiatan')

# View untuk menghapus peserta kegiatan
@permission_required('data.delete_pesertakegiatan')
def peserta_kegiatan_form_delete(request, pk):
  if request.method == 'GET':
    log_activity(request)
  return deleteData(request, PesertaKegiatan, pk, 'peserta_kegiatan_list', 'data_pesertakegiatan')

# 🚨FOTO KEGIATAN🚨
# View dari daftar foto kegiatan
@permission_required('data.view_fotokegiatan')
def fotoKegiatanList(request):
  if request.method == 'GET':
    log_activity(request)

  num_page = 20
  
  query = ''
  page = ''

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

# View dari daftar foto kegiatan mode observer
@permission_required('data.view_fotokegiatan')
def fotoKegiatanListObserver(request):
  if request.method == 'GET':
    log_activity(request)

  num_page = 20
  
  query = ''
  page = ''
  profile = Profile.objects.filter(user=request.user).values_list('user_observed', flat=True)

  if 'q' in request.GET:
    query = request.GET['q']
    data = FotoKegiatan.objects.filter(kegiatan__nama__icontains=query, user__in=profile)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)
  
  else:
    data = FotoKegiatan.objects.filter(user__in=profile)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)

  return render(request, 'forms/lists/kegiatan_foto_observer.html', {'dataset': data_page, 'page': page, 'query': query})

# Form untuk menambahkan dan mengubah foto kegiatan
class fotoKegiatanForm(forms.ModelForm):
  class Meta:
    model = FotoKegiatan
    fields = ('kegiatan', 'foto')
    widgets = {
      'kegiatan': forms.TextInput(),
      'foto': forms.ClearableFileInput(attrs={'multiple': True})
    }

# Form untuk komentar foto kegiatan
class fotoKegiatanFormComment(forms.ModelForm):
  class Meta:
    model = FotoKegiatan
    fields = ('user',)

# View dari form penambahan foto kegiatan, tidak menggunakan template karena ada fitur upload banyak file
@permission_required('data.add_fotokegiatan')
def foto_kegiatan_form_add(request):
  if request.method == 'GET':
    log_activity(request)

  # LOGIKA UNTUK TIPE DEVICE
  if request.user_agent.device.family == None:
    device_type = 'None'
  else:
    device_type=request.user_agent.device.family

  # KIRIM KE DATABASE
  if request.method == 'POST':
    form = fotoKegiatanForm(request.POST, request.FILES)
    images = request.FILES.getlist('foto')

    if form.is_valid():
      post = form.save(commit= False)
      if images:  #check if user has uploaded some files
        for img in images:
          # KIRIM DB FOTO KEGIATAN
          FotoKegiatan.objects.create(kegiatan=post.kegiatan, foto=img, user=request.user)

          # KIRIM DB DATA LOGS
          DataLog.objects.create(
            action='INSERT',
            dataset='data_fotokegiatan',
            id_dataset=post.id,
            user=request.user,
            ip_user=request.META.get('REMOTE_ADDR'),
            device_user=device_type,
            os_user=request.user_agent.os.family,
            browser_user=request.user_agent.browser.family)
      return redirect('foto_kegiatan_list')
  
  else:
    form = fotoKegiatanForm()

  return render(request, 'forms/form/kegiatan_foto_add.html', {'form': form})

# View dari form perubahan foto kegiatan
@permission_required('data.change_fotokegiatan')
def foto_kegiatan_form_update(request, pk):
  if request.method == 'GET':
    log_activity(request)
  return updateData(request, FotoKegiatan, pk, fotoKegiatanForm, 'foto_kegiatan_list', 'forms/form/kegiatan_foto_update.html', 'data_fotokegiatan')

# View dari form perubahan foto kegiatan
@permission_required('data.change_fotokegiatan')
def foto_kegiatan_form_comment(request, pk):
  if request.method == 'GET':
    log_activity(request)
  return commentData(request, FotoKegiatan, pk, fotoKegiatanFormComment, 'foto_kegiatan_list', 'forms/form/kegiatan_foto_update.html', 'data_fotokegiatan')

# View untuk menghapus foto kegiatan
@permission_required('data.delete_fotokegiatan')
def foto_kegiatan_form_delete(request, pk):
  if request.method == 'GET':
    log_activity(request)
  return deleteData(request, FotoKegiatan, pk, 'foto_kegiatan_list', 'data_fotokegiatan')

urlpatterns = [
  path('dict/kegiatan/', kegiatan_dict, name='kegiatan_dict'),
  path('forms/kegiatan/', kegiatanList, name='kegiatan_list'),
  path('forms/kegiatan/observer/', kegiatanListObserver, name='kegiatan_list_observer'),
  path('forms/kegiatan/<uuid:pk>/', kegiatanDetail, name='kegiatan_detail'),
  path('forms/kegiatan-add/', kegiatan_form_add, name='kegiatan_form_add'),
  path('forms/kegiatan-update/<uuid:pk>/', kegiatan_form_update, name='kegiatan_form_update'),
  path('forms/kegiatan-comment/<uuid:pk>/', kegiatan_form_comment, name='kegiatan_form_comment'),
  path('forms/kegiatan-delete/<uuid:pk>/', kegiatan_form_delete, name='kegiatan_form_delete'),

  path('forms/kegiatan/peserta/', pesertaKegiatanList, name='peserta_kegiatan_list'),
  path('forms/kegiatan/peserta/observer/', pesertaKegiatanListObserver, name='peserta_kegiatan_list_observer'),
  path('forms/kegiatan/peserta-add/', peserta_kegiatan_form_add, name='peserta_kegiatan_form_add'),
  path('forms/kegiatan/peserta-update/<uuid:pk>/', peserta_kegiatan_form_update, name='peserta_kegiatan_form_update'),
  path('forms/kegiatan/peserta-comment/<uuid:pk>/', peserta_kegiatan_form_comment, name='peserta_kegiatan_form_comment'),
  path('forms/kegiatan/peserta-delete/<uuid:pk>/', peserta_kegiatan_form_delete, name='peserta_kegiatan_form_delete'),

  path('forms/kegiatan/foto/', fotoKegiatanList, name='foto_kegiatan_list'),
  path('forms/kegiatan/foto/observer/', fotoKegiatanListObserver, name='foto_kegiatan_list_observer'),
  path('forms/kegiatan/foto-add/', foto_kegiatan_form_add, name='foto_kegiatan_form_add'),
  path('forms/kegiatan/foto-update/<uuid:pk>/', foto_kegiatan_form_update, name='foto_kegiatan_form_update'),
  path('forms/kegiatan/foto-comment/<uuid:pk>/', foto_kegiatan_form_comment, name='foto_kegiatan_form_comment'),
  path('forms/kegiatan/foto-delete/<uuid:pk>/', foto_kegiatan_form_delete, name='foto_kegiatan_form_delete'),
]