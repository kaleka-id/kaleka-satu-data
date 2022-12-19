from django.contrib.auth.decorators import permission_required
from django.forms import ModelForm
from django.urls import path
from operation.data_modification import listData, listSpatialData, detailData, addData, updateData, deleteData
from data.dataset.testing import Testing, Shop
from leaflet.forms.widgets import LeafletWidget


# 🚨DATASET ARTIKEL🚨
# View dari daftar artikel
@permission_required('data.view_testing')
def testingArtikel(request):
  return listData(request, Testing, 'lists/testing_artikel.html', 'artikel')

# View dari informasi detil artikel
@permission_required('data.view_testing')
def testingArtikelDetail(request, pk):
  return detailData(request, Testing, pk, 'details/testing_artikel.html', 'artikel')

# Form untuk menambahkan dan mengubah artikel
class testingArtikelForm(ModelForm):
  class Meta:
    model = Testing
    fields = ('kode', 'nama', 'deskripsi')

# View dari form penambahan artikel
@permission_required('data.add_testing')
def article_form_add(request):
  return addData(request, testingArtikelForm, 'testing_artikel_list', 'forms/testing_artikel_add.html')

# View dari form perubahan artikel
@permission_required('data.change_testing')
def article_form_update(request, pk):
  return updateData(request, Testing, pk, testingArtikelForm, 'testing_artikel_list', 'forms/testing_artikel_update.html')

# View untuk menghapus artikel
@permission_required('data.delete_testing')
def article_form_delete(request, pk):
  return deleteData(request, Testing, pk, 'testing_artikel_list')

# 🚨DATASET SHOP🚨
# View dari daftar toko
@permission_required('data.view_shop')
def testingShop(request):
  return listData(request, Shop, 'lists/testing_shop.html', 'toko')

def testingShopJSON(request):
  return listSpatialData(request, Shop)

# View dari informasi detil toko
@permission_required('data.view_shop')
def testingShopDetail(request, pk):
  return detailData(request, Shop, pk, 'details/testing_shop.html', 'toko')

# Form untuk menambahkan dan mengubah toko
class testingShopForm(ModelForm):
  class Meta:
    model = Shop
    fields = ('name_shop', 'geom', 'address', 'Open', 'capacity')
    widgets = {
      'geom': LeafletWidget()
    }

# View dari form penambahan toko
@permission_required('data.add_shop')
def shop_form_add(request):
  return addData(request, testingShopForm, 'testing_toko_list', 'forms/testing_toko_add.html')

# View dari form perubahan toko
@permission_required('data.change_shop')
def shop_form_update(request, pk):
  return updateData(request, Shop, pk, testingShopForm, 'testing_toko_list', 'forms/testing_toko_update.html')

# View untuk menghapus toko
@permission_required('data.delete_shop')
def shop_form_delete(request, pk):
  return deleteData(request, Shop, pk, 'testing_toko_list')

# URL pada setiap view
urlpatterns = [
  path('forms/testing-artikel/', testingArtikel, name='testing_artikel_list'),
  path('forms/testing-artikel/<uuid:pk>/', testingArtikelDetail, name='testing_artikel_detail'),
  path('forms/testing-artikel-add/', article_form_add, name='testing_artikel_form'),
  path('forms/testing-artikel-update/<uuid:pk>/', article_form_update, name='testing_artikel_form_update'),
  path('forms/testing-artikel-delete/<uuid:pk>/', article_form_delete, name='testing_artikel_form_delete'),

  path('forms/testing-toko/', testingShop, name='testing_toko_list'),
  path('forms/testing-toko-json/', testingShopJSON, name='testing_toko_json'),
  path('forms/testing-toko/<int:pk>/', testingShopDetail, name='testing_toko_detail'),
  path('forms/testing-toko-add/', shop_form_add, name='testing_toko_form'),
  path('forms/testing-toko-update/<int:pk>/', shop_form_update, name='testing_toko_form_update'),
  path('forms/testing-toko-delete/<int:pk>/', shop_form_delete, name='testing_toko_form_delete'),
]