from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "main/index.html")

@login_required
def profile_view(request):
    return render(request, "auth/profile.html")

@login_required
def settings_view(request):
    return render(request, "settings page/index.html")
