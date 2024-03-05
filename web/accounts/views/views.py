import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from accounts.models import CustomUser


@login_required
def username_page(request, username):
    return render(request, 'registration/username.html', {'username': username})

@login_required
def custom_logout(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', 'home'))



