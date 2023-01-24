from operation.ops_models.profiles import Profile

def profil(request):
  if request.user.is_authenticated:
    profile = Profile.objects.filter(user=request.user)
    return {'profil': profile}
  else:
    profile = Profile.objects.none()
    return {'profil': profile}