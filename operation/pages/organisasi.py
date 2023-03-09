from django.shortcuts import render, get_object_or_404
from django.urls import path
from operation.signals import log_activity
from data.dataset.organisasi import Organisasi, NamaOrganisasi
from django.db.models import Q

def organisasiDict(request):
  if request.method == 'GET':
    log_activity(request)

  q = ''
  page = ''

  if 'q' in request.GET:
    q = request.GET['q']
    
  # pre_data = Organisasi.objects.filter(nama_organisasi__icontains=q)
  pre_data = Organisasi.objects.all()

  
  from django.db.models import Count
  for item in pre_data:
    kode = item.alamat.kode_desa
    # pre_data2 = Organisasi.objects.filter(kode__icontains=f'ORG-{kode}')
    x = kode
    y = Organisasi.objects.filter(alamat__kode_desa=kode).count()
    z = ''
    print(f'{x} | {y} | {z}')

  # number = pre_data.count() + 1
  # return f'ORG-{kode}-{number}'


  #   data = Organisasi.objects.filter(id=pre_data.id)
  #   p = Paginator(data, 20)
  #   page = request.GET.get('page')
  #   data_page = p.get_page(page)
  # else:
  #   data_page = Orang.objects.none()

  return render(request, 'dictionary/organisasi.html', {
    # 'dataset': data_page, 
    # 'query': q, 
    # 'page': page
  })

def organisasiList(request):
  if request.method == 'GET':
    log_activity(request)
  
  organisasi = Organisasi.objects.filter(user=request.user)
  return render(request, 'forms/lists/organisasi.html', {'dataset': organisasi})

# View dari informasi detil organisasi
# @permission_required('data.view_lahan')
def organisasiDetail(request, pk):
  if request.method == 'GET':
    log_activity(request)
  
  organisasi = get_object_or_404(Organisasi, id=pk)
  nama = NamaOrganisasi.objects.filter(organisasi=organisasi.id)
  return render(request, 'forms/details/organisasi.html', {
    'organisasi': organisasi,
    'nama': nama,
  })

urlpatterns = [
  path('dict/organisasi/', organisasiDict, name='organisasi_dict'),
  path('forms/organisasi/', organisasiList, name='organisasi_list'),
  path('forms/organisasi/<uuid:pk>/', organisasiDetail, name='organisasi_detail'),
]