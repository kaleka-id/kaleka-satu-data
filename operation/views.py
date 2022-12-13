from django.shortcuts import render, HttpResponse
from .forms import loginForm
from django.contrib.auth import authenticate, login

# Create your views here.
def userLogin(request):
  if request.method == "POST":
    form = loginForm(request.POST)

    if form.is_valid():
      cd = form.cleaned_data
      user = authenticate(request, username = cd['username'], password = cd['password'])

      if user is not None:
        login(request, user)
        return HttpResponse('You are authenticated')

      else:
        return HttpResponse('Invalid Login')
    
  else:
    form = loginForm()

  return render(request, 'account/login.html', {'form': form})