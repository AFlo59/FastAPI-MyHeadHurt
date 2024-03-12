import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from accounts.models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.forms import UserUpdateForm

@login_required
def username_page(request, username):
    user = request.user

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('username', username=username)
        else:
            messages.error(request, 'An error occurred while updating your account.')
    else:
        form = UserUpdateForm(instance=user)

    context = {
        'user': user,
        'form': form,
    }
    return render(request, 'registration/username.html', context)

@login_required
def custom_logout(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', 'home'))



