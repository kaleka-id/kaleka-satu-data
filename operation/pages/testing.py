from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from data.dataset.testing import Testing

# View dari daftar artikel
@login_required
def testingArtikel(request):
  desc = Testing.objects.filter(user=request.user)
  return render(request, 'lists/testing_artikel.html', {
    'artikel': desc
  })

# View dari informasi detil artikel
@login_required
def testingArtikelDetail(request, slug):
  desc = get_object_or_404(Testing, slug=slug)
  return render(request, 'details/testing_artikel.html', {
    'artikel': desc
  })

# form untuk menambahkan artikel
class testingArtikelForm(ModelForm):
  class Meta:
    model = Testing
    fields = ('kode', 'nama', 'deskripsi')

# View dari form penambahan artikel
def article_form(request):
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