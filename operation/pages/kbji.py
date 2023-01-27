from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.urls import path
from django.shortcuts import render
from django.db.models import Q
from data.dataset.kbji import KBJI
from operation.signals import log_activity

@permission_required('data.search_kbji')
def KBJI_dict(request):
  log_activity(request)

  q = None
  page = None

  if 'q' in request.GET:
    q = request.GET['q']
    data = KBJI.objects.filter(
      Q(golongan_pokok__icontains=q) | 
      Q(subgolongan_pokok__icontains=q) |
      Q(golongan__icontains=q) |
      Q(subgolongan__icontains=q) |
      Q(jabatan__icontains=q)).order_by('kode_jabatan')
    p = Paginator(data, 20)
    page = request.GET.get('page')
    data_page = p.get_page(page)
  else:
    data_page = KBJI.objects.none()

  return render(request, 'dictionary/kbji.html', {'dataset': data_page, 'query': q, 'page': page})

urlpatterns = [
  path('dict/kbji/', KBJI_dict, name='KBJI_dict'),
]