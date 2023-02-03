from django.contrib.auth.decorators import permission_required
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from django.urls import path
from django.shortcuts import render
from django.db.models import Q
from data.dataset.alamat import Alamat
from operation.signals import log_activity

@permission_required('data.search_alamat')
def alamat_dict(request):
  if request.method == 'GET':
    log_activity(request)

  q = ''
  page = ''

  if 'q' in request.GET:
    q = request.GET['q']
    data = Alamat.objects.filter(
      Q(nama_prov__icontains=q) | 
      Q(nama_kabkot__icontains=q) |
      Q(nama_kec__icontains=q) |
      Q(nama_desa__icontains=q)).order_by('nama_desa')
    p = Paginator(data, 20)
    page = request.GET.get('page')
    data_page = p.get_page(page)
  else:
    data_page = Alamat.objects.none()

  return render(request, 'dictionary/alamat.html', {'dataset': data_page, 'query': q, 'page': page})

urlpatterns = [
  path('dict/alamat/', alamat_dict, name='alamat_dict'),
]