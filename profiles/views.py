from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from .models import Profile

def profile(request, username):
    profiles = Profile.objects.all()
    return render(request, 'profile.html', {'username': username, 'profiles': profiles})