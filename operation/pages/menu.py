from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path
from ..models import Forms

def home(request):
    return render(request, 'menu/home.html')

@permission_required('operation.view_forms')
def forms(request):
  desc = Forms.objects.all()
  return render(request, 'menu/forms.html', {
    'forms': desc
  })

urlpatterns = [
  path('', home, name='home'),
  path('forms/', forms, name='forms'),
]