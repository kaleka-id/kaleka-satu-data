from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from data.dataset.testing import Testing

@login_required
def testingArtikel(request):
  desc = Testing.objects.filter(user=request.user)
  return render(request, 'lists/testing_artikel.html', {
    'artikel': desc
  })

def testingArtikelDetail(request, slug):
  desc = get_object_or_404(Testing, slug=slug)
  return render(request, 'details/testing_artikel.html', {
    'artikel': desc
  })