from django.shortcuts import render, redirect, get_object_or_404
from django.core.serializers import serialize
from django.http import HttpResponse

# LIST OF DATA MODIFICATION FUNCTIONS
def listData(request, dataset, url, callback):
  data = dataset.objects.filter(user=request.user)
  return render(request, url, {callback: data})

def listSpatialData(request, dataset):
  place = serialize('geojson', dataset.objects.filter(user=request.user))
  return HttpResponse(place, content_type='json')

def detailData(request, dataset, pk, url, callback):
  desc = get_object_or_404(dataset, id=pk)
  return render(request, url, {callback: desc})

def addData(request, forms, redirects, url):
  if request.method == 'POST':
    form = forms(request.POST)
    if form.is_valid():
      artikel = form.save(commit= False)
      artikel.user = request.user
      artikel.save()
      form.save_m2m()
      return redirect(redirects)
  
  else:
    form = forms()

  return render(request, url, {
    'form': form 
  })

def updateData(request, dataset, pk, forms, redirects, url):
  artikel = get_object_or_404(dataset, id=pk)
  form = forms(request.POST or None, instance=artikel)
  if form.is_valid():
    form.save()
    return redirect(redirects)

  return render(request, url, {'form':form})

def deleteData(request, dataset, pk, redirects):
  artikel = get_object_or_404(dataset, id=pk)
  artikel.delete()
  return redirect(redirects)