from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.urls import path
from django.shortcuts import render
from django.db.models import Q
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

urlpatterns = [
  path('dict/kegiatan/', kegiatan_dict, name='kegiatan_dict'),
]