from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path
from ..models import Forms, Docs, Dictionary
from ..data_modification import detailData

def home(request):
    return render(request, 'menu/home.html')

@permission_required('operation.view_forms')
def forms(request):
  desc = Forms.objects.all()
  return render(request, 'menu/forms.html', {
    'forms': desc
  })

@permission_required('operation.view_docs')
def docs(request):
  desc = Docs.objects.all()
  return render(request, 'menu/docs.html', {
    'docs': desc
  })

@permission_required('operation.view_docs')
def docs_detail(request, pk):
  return detailData(request, Docs, pk, 'menu/docs_detail.html', 'docs')

@permission_required('operation.view_docs')
def dictionary(request):
  desc = Dictionary.objects.all()
  return render(request, 'menu/dictionary.html', {
    'dict': desc
  })

urlpatterns = [
  path('', home, name='home'),
  path('forms/', forms, name='forms'),
  path('docs/', docs, name='docs'),
  path('docs/<int:pk>/', docs_detail, name='docs_detail'),
  path('dict/', dictionary, name='dictionary'),
]