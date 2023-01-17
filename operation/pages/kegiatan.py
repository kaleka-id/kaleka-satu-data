from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.urls import path
from django.shortcuts import render, get_object_or_404
from operation.data_modification import geojsonData, detailData, addData, updateData, deleteData
from data.dataset.kegiatan import Kegiatan, PesertaKegiatan, FotoKegiatan

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

# View dari informasi detil orang
@permission_required('data.view_orang')
def kegiatanDetail(request, pk):
  kegiatan = get_object_or_404(Kegiatan, id=pk)
  peserta = PesertaKegiatan.objects.filter(kegiatan=pk)
  foto = FotoKegiatan.objects.filter(kegiatan=pk)
  return render(request, 'forms/details/kegiatan.html', {
    'kegiatan': kegiatan, 
    'peserta': peserta,
    'foto': foto})

urlpatterns = [
  path('dict/kegiatan/', kegiatan_dict, name='kegiatan_dict'),
  path('forms/kegiatan/', kegiatanList, name='kegiatan_list'),
  path('forms/kegiatan/<uuid:pk>/', kegiatanDetail, name='kegiatan_detail'),
]