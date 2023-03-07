from django.shortcuts import render, get_object_or_404
from django.urls import path
from operation.signals import log_activity
from data.dataset.organisasi import Organisasi, NamaOrganisasi

def organisasiList(request):
  if request.method == 'GET':
    log_activity(request)
  
  organisasi = Organisasi.objects.filter(user=request.user)
  nama = NamaOrganisasi.objects.filter(user=request.user)
  return render(request, 'forms/lists/organisasi.html', {
    'dataset': organisasi,
    'nama': nama,
  })

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
    path('forms/organisasi/', organisasiList, name='organisasi_list'),
    path('forms/organisasi/<uuid:pk>/', organisasiDetail, name='organisasi_detail'),
]