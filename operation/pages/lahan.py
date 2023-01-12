from django import forms
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import path
from django.shortcuts import render
from operation.data_modification import detailData, addData, updateData, deleteData
from data.dataset.lahan import Lahan

# DICTIONARY
@permission_required('data.search_lahan')
def lahan_dict(request):
  q = None
  page = None

  if 'q' in request.GET:
    q = request.GET['q']
    data = Lahan.objects.filter(petani__nama_lengkap__icontains=q)
    p = Paginator(data, 1)
    page = request.GET.get('page')
    data_page = p.get_page(page)
  else:
    data_page = Lahan.objects.none()

  return render(request, 'dictionary/lahan.html', {'dataset': data_page, 'query': q, 'page': page})


urlpatterns = [
  path('dict/lahan/', lahan_dict, name='lahan_dict'),
]