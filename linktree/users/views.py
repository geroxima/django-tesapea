from django.shortcuts import render
from .models import UserProfile

def user_profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'user_profile_list.html', {'profiles': profiles})

def main_page(request):
    profiles = UserProfile.objects.all()
    return render(request, 'main_page.html', {'profiles': profiles})

def user_profile_detail(request, profile_id):
    profile = UserProfile.objects.get(id=profile_id)
    return render(request, 'user_profile_detail.html', {'profile': profile})