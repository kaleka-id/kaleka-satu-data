from operation.models import Profile

def profil(request):
  profile = Profile.objects.filter(user=request.user)
  return {'profil': profile}