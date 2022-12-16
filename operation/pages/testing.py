from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.forms import ModelForm
from django.urls import path
from django.core.serializers import serialize
from django.http import HttpResponse
from data.dataset.testing import Testing, Shop

# Fungsi reusable, nanti dibuat file python sendiri
def listData(request, dataset, url, callback):
  data = dataset.objects.filter(user=request.user)
  return render(request, url, {callback: data})

def listSpatialData(request, dataset):
  place = serialize('geojson', dataset.objects.filter(user=request.user))
  return HttpResponse(place, content_type='json')

# 🚨DATASET ARTIKEL🚨
# View dari daftar artikel
@permission_required('data.view_testing')
def testingArtikel(request):
  return listData(request, Testing, 'lists/testing_artikel.html', 'artikel')

# View dari informasi detil artikel
@permission_required('data.view_testing')
def testingArtikelDetail(request, slug):
  desc = get_object_or_404(Testing, slug=slug)
  return render(request, 'details/testing_artikel.html', {
    'artikel': desc
  })

# form untuk menambahkan dan mengubah artikel
class testingArtikelForm(ModelForm):
  class Meta:
    model = Testing
    fields = ('kode', 'nama', 'deskripsi')

# View dari form penambahan artikel
@permission_required('data.add_testing')
def article_form_add(request):
  if request.method == 'POST':
    form = testingArtikelForm(request.POST)
    if form.is_valid():
      artikel = form.save(commit= False)
      artikel.user = request.user
      artikel.save()
      return redirect('testing_artikel_list')
  
  else:
    form = testingArtikelForm()

  return render(request, 'forms/testing_artikel_add.html', {
    'form': form 
  })

# View dari form perubahan artikel
@permission_required('data.change_testing')
def article_form_update(request, slug):
  artikel = get_object_or_404(Testing, slug=slug)
  form = testingArtikelForm(request.POST or None, instance=artikel)
  if form.is_valid():
    form.save()
    return redirect('testing_artikel_list')

  return render(request, 'forms/testing_artikel_update.html', {
    'form':form
  })

# View untuk menghapus artikel
@permission_required('data.delete_testing')
def article_form_delete(request, slug):
  artikel = get_object_or_404(Testing, slug=slug)
  artikel.delete()
  return redirect('testing_artikel_list')

# 🚨DATASET SHOP🚨
# View dari daftar 
@permission_required('data.view_shop')
def testingShop(request):
  return listData(request, Shop, 'lists/testing_shop.html', 'toko')

def testingShopJSON(request):
  return listSpatialData(request, Shop)


# View dari informasi detil artikel
@permission_required('data.view_shop')
def testingShopDetail(request, slug):
  desc = get_object_or_404(Shop, slug=slug)
  return render(request, 'details/testing_shop.html', {
    'toko': desc
  })

# URL pada setiap view
urlpatterns = [
  path('forms/testing-artikel/', testingArtikel, name='testing_artikel_list'),
  path('forms/testing-artikel/<slug:slug>/', testingArtikelDetail, name='testing_artikel_detail'),
  path('forms/testing-artikel-add/', article_form_add, name='testing_artikel_form'),
  path('forms/testing-artikel-update/<slug:slug>/', article_form_update, name='testing_artikel_form_update'),
  path('forms/testing-artikel-delete/<slug:slug>/', article_form_delete, name='testing_artikel_form_delete'),

  path('forms/testing-toko/', testingShop, name='testing_toko_list'),
  path('forms/testing-toko-json/', testingShopJSON, name='testing_toko_json'),
  path('forms/testing-toko/<slug:slug>/', testingShopDetail, name='testing_toko_detail'),
]