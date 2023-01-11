from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.urls import path
from django.shortcuts import render
from data.dataset.orang import Orang

@permission_required('data.search_orang')
def orang_dict(request):
  q = None
  page = None

  if 'q' in request.GET:
    q = request.GET['q']
    data = Orang.objects.filter(nama_lengkap__icontains=q).order_by('nama_lengkap')
    p = Paginator(data, 20)
    page = request.GET.get('page')
    data_page = p.get_page(page)
  else:
    data_page = Orang.objects.none()

  return render(request, 'dictionary/orang.html', {'dataset': data_page, 'query': q, 'page': page})

urlpatterns = [
  path('dict/orang/', orang_dict, name='orang_dict'),
]