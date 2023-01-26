from django import forms
from django.contrib.auth.decorators import permission_required
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.urls import path
from django.db.models import Q
from django.core.paginator import Paginator
from operation.data_modification import geojsonData, detailData, addData, updateData, deleteData
from data.dataset.testing import Testing, Shop, Product
from leaflet.forms.widgets import LeafletWidget

from django.shortcuts import render


# 🚨DATASET ARTIKEL🚨
# View dari daftar artikel
@permission_required('data.view_testing')
def testingArtikel(request):
  num_page = 20
  
  query = None
  page = None

  if 'q' in request.GET:
    query = request.GET['q']
    data = Testing.objects.filter(user=request.user, nama__icontains=query)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)
  
  else:
    data = Testing.objects.filter(user=request.user)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)

  return render(request, 'forms/lists/testing_artikel.html', {'dataset': data_page, 'page': page, 'query': query})

# View dari informasi detil artikel
@permission_required('data.view_testing')
def testingArtikelDetail(request, pk):
  return detailData(request, Testing, pk, 'forms/details/testing_artikel.html', 'artikel')

# Form untuk menambahkan dan mengubah artikel
class testingArtikelForm(forms.ModelForm):
  class Meta:
    model = Testing
    fields = ('kode', 'nama', 'deskripsi')

# View dari form penambahan artikel
@permission_required('data.add_testing')
def article_form_add(request):
  return addData(request, testingArtikelForm, 'testing_artikel_list', 'forms/form/testing_artikel_add.html', 'data_testing')

# View dari form perubahan artikel
@permission_required('data.change_testing')
def article_form_update(request, pk):
  return updateData(request, Testing, pk, testingArtikelForm, 'testing_artikel_list', 'forms/form/testing_artikel_update.html', 'data_testing')

# View untuk menghapus artikel
@permission_required('data.delete_testing')
def article_form_delete(request, pk):
  return deleteData(request, Testing, pk, 'testing_artikel_list', 'data_testing')

# Dictionary artikel
def article_dict(request):
  if 'q' in request.GET:
    q = request.GET['q']
    data = Testing.objects.filter(nama__icontains=q)
  else:
    data = Testing.objects.none()
  return render(request, 'dictionary/testing_artikel.html', {'artikel': data})

# 🚨DATASET SHOP🚨
# View dari daftar toko
@permission_required('data.view_shop')
def testingShop(request):
  num_page = 20
  
  query = None
  page = None

  if 'q' in request.GET:
    query = request.GET['q']
    data = Shop.objects.filter(user=request.user, name_shop__icontains=query)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)
  
  else:
    data = Shop.objects.filter(user=request.user)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)

  return render(request, 'forms/lists/testing_shop.html', {'dataset': data_page, 'page': page, 'query': query})

def testingShopJSON(request):
  return geojsonData(request, Shop)

# View dari informasi detil toko
@permission_required('data.view_shop')
def testingShopDetail(request, pk):
  return detailData(request, Shop, pk, 'forms/details/testing_shop.html', 'toko')

# Form untuk menambahkan dan mengubah toko
class testingShopForm(forms.ModelForm):
  class Meta:
    model = Shop
    fields = ('name_shop', 'geom', 'address', 'Open', 'capacity')
    widgets = {
      'geom': LeafletWidget()
    }

# View dari form penambahan toko
@permission_required('data.add_shop')
def shop_form_add(request):
  return addData(request, testingShopForm, 'testing_toko_list', 'forms/form/testing_toko_add.html', 'data_shop')

# View dari form perubahan toko
@permission_required('data.change_shop')
def shop_form_update(request, pk):
  return updateData(request, Shop, pk, testingShopForm, 'testing_toko_list', 'forms/form/testing_toko_update.html', 'data_shop')

# View untuk menghapus toko
@permission_required('data.delete_shop')
def shop_form_delete(request, pk):
  return deleteData(request, Shop, pk, 'testing_toko_list', 'data_shop')

# Dictionary toko
def shop_dict(request):
  if 'q' in request.GET:
    q = request.GET['q']
    data = Shop.objects.filter(Q(name_shop__icontains=q) | Q(address__icontains=q))
  else:
    data = Shop.objects.none()
  return render(request, 'dictionary/testing_toko.html', {'toko': data})


# 🚨DATASET PRODUK🚨
# View dari daftar produk
@permission_required('data.view_product')
def testingProduct(request):
  num_page = 20
  
  query = None
  page = None

  if 'q' in request.GET:
    query = request.GET['q']
    data = Product.objects.filter(user=request.user, nama__icontains=query)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)
  
  else:
    data = Product.objects.filter(user=request.user)
    p = Paginator(data, num_page)
    page = request.GET.get('page')
    data_page = p.get_page(page)

  return render(request, 'forms/lists/testing_produk.html', {'dataset': data_page, 'page': page, 'query': query})

# View dari informasi detil artikel
@permission_required('data.view_product')
def testingProductDetail(request, pk):
  return detailData(request, Product, pk, 'forms/details/testing_produk.html', 'produk')

# Form untuk menambahkan dan mengubah artikel
class testingProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = ('nama', 'deskripsi', 'foto', 'toko')
    widgets = {
      'deskripsi': forms.TextInput(),
      # 'toko': forms.SelectMultiple()
      'toko': forms.CheckboxSelectMultiple(),
    }
  
# View dari form penambahan produk
@permission_required('data.add_product')
def product_form_add(request):
  return addData(request, testingProductForm, 'testing_produk_list', 'forms/form/testing_produk_add.html', 'data_product')

# View dari form perubahan produk
@permission_required('data.change_product')
def product_form_update(request, pk):
  return updateData(request, Product, pk, testingProductForm, 'testing_produk_list', 'forms/form/testing_produk_update.html', 'data_product')

# View untuk menghapus produk
@permission_required('data.delete_product')
def product_form_delete(request, pk):
  return deleteData(request, Product, pk, 'testing_produk_list', 'data_product')

# Dictionary produk
def product_dict(request):
  if 'q' in request.GET:
    q = request.GET['q']
    data = Product.objects.filter(nama__icontains=q)
  else:
    data = Product.objects.none()
  return render(request, 'dictionary/testing_produk.html', {'produk': data})

# URL pada setiap view
urlpatterns = [
  path('forms/testing-artikel/', testingArtikel, name='testing_artikel_list'),
  path('forms/testing-artikel/<uuid:pk>/', testingArtikelDetail, name='testing_artikel_detail'),
  path('forms/testing-artikel-add/', article_form_add, name='testing_artikel_form'),
  path('forms/testing-artikel-update/<uuid:pk>/', article_form_update, name='testing_artikel_form_update'),
  path('forms/testing-artikel-delete/<uuid:pk>/', article_form_delete, name='testing_artikel_form_delete'),
  path('dict/testing-artikel/', article_dict, name='testing_artikel_dict'),

  path('forms/testing-toko/', testingShop, name='testing_toko_list'),
  path('forms/testing-toko-json/', testingShopJSON, name='testing_toko_json'),
  path('forms/testing-toko/<int:pk>/', testingShopDetail, name='testing_toko_detail'),
  path('forms/testing-toko-add/', shop_form_add, name='testing_toko_form'),
  path('forms/testing-toko-update/<int:pk>/', shop_form_update, name='testing_toko_form_update'),
  path('forms/testing-toko-delete/<int:pk>/', shop_form_delete, name='testing_toko_form_delete'),
  path('dict/testing-toko/', shop_dict, name='testing_toko_dict'),

  path('forms/testing-produk/', testingProduct, name='testing_produk_list'),
  path('forms/testing-produk/<uuid:pk>/', testingProductDetail, name='testing_produk_detail'),
  path('forms/testing-produk-add/', product_form_add, name='testing_produk_form'),
  path('forms/testing-produk-update/<uuid:pk>/', product_form_update, name='testing_produk_form_update'),
  path('forms/testing-produk-delete/<uuid:pk>/', product_form_delete, name='testing_produk_form_delete'),
  path('dict/testing-produk/', product_dict, name='testing_produk_dict'),
]