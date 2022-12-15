from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from ..models import Forms

def home(request):
    return render(request, 'menu/home.html')

# def forms(request):
#     return render(request, 'menu/forms.html')

@permission_required('operation.view_forms')
def forms(request):
  desc = Forms.objects.all()
  return render(request, 'menu/forms.html', {
    'forms': desc
  })