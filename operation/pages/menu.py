from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path
from ..models import Forms, Docs, Dictionary, Dashboard, Catalog
from ..data_modification import detailData

def home(request):
    return render(request, 'menu/home.html')

@permission_required('operation.view_forms')
def forms(request):
  desc = Forms.objects.all().order_by('nama')
  return render(request, 'menu/forms.html', {
    'forms': desc
  })

@permission_required('operation.view_docs')
def docs(request):
  desc = Docs.objects.all().order_by('judul')
  return render(request, 'menu/docs.html', {
    'docs': desc
  })

@permission_required('operation.view_docs')
def docs_detail(request, pk):
  return detailData(request, Docs, pk, 'menu/docs_detail.html', 'docs')

@permission_required('operation.view_docs')
def dictionary(request):
  desc = Dictionary.objects.all().order_by('nama')
  return render(request, 'menu/dictionary.html', {
    'dict': desc
  })

@login_required
def dashboard(request):
  desc = Dashboard.objects.all().order_by('nama')
  return render(request, 'menu/dashboard.html', {
    'dashboard': desc
  })

@login_required
def dashboard_detail(request, pk):
  return detailData(request, Dashboard, pk, 'menu/dashboard_detail.html', 'dashboard')

@login_required
def catalog(request):
  desc = Catalog.objects.all().order_by('nama')
  return render(request, 'menu/catalog.html', {
    'catalog': desc
  })

@login_required
def catalog_detail(request, pk):
  return detailData(request, Catalog, pk, 'menu/catalog_detail.html', 'catalog')

@login_required
def about(request):
  return render(request, 'menu/about.html')

@login_required
def about_geoserver_qgis(request):
  return render(request, 'menu/tutorial/geoserver_qgis.html')

urlpatterns = [
  path('', home, name='home'),
  path('forms/', forms, name='forms'),
  path('docs/', docs, name='docs'),
  path('docs/<int:pk>/', docs_detail, name='docs_detail'),
  path('dict/', dictionary, name='dictionary'),
  path('dashboard/', dashboard, name='dashboard'),
  path('dashboard/<int:pk>/', dashboard_detail, name='dashboard_detail'),
  path('catalog/', catalog, name='catalog'),
  path('catalog/<int:pk>/', catalog_detail, name='catalog_detail'),
  path('about/', about, name='about'),
  path('about/tutorial-geoserver-di-qgis', about_geoserver_qgis, name='about_geoserver_qgis'),
]