from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.urls import path
from django.shortcuts import render
from data.dataset.profesi import Profesi
from operation.signals import log_activity

@permission_required('data.search_profesi')
def profesi_dict(request):
  log_activity(request)
  
  q = None
  page = None

  if 'q' in request.GET:
    q = request.GET['q']
    data = Profesi.objects.filter(nama__icontains=q).order_by('nama')
    p = Paginator(data, 20)
    page = request.GET.get('page')
    data_page = p.get_page(page)
  else:
    data_page = Profesi.objects.none()

  return render(request, 'dictionary/profesi.html', {'dataset': data_page, 'query': q, 'page': page})

urlpatterns = [
  path('dict/profesi/', profesi_dict, name='profesi_dict'),
]