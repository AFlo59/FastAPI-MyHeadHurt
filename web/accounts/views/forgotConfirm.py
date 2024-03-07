from django.shortcuts import render, redirect
from django.contrib.auth import password_reset_confirm
from django.contrib.messages import messages
from django.contrib.auth.forms import SetPasswordForm
from accounts.models import CustomUser

def reset_password_confirm(request, uidb64, token):
    if request.method == 'POST':
        form = SetPasswordForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.get_by_natural_key(uidb64)
            if password_reset_confirm(request, uidb64=uidb64, token=token):
                user.set_password(form.cleaned_data['new_password1'])
                user.save()
                messages.success(request, 'Your password has been reset successfully.')
                return redirect('login')
            else:
                messages.error(request, 'Invalid token or expired link.')
    else:
        form = SetPasswordForm()

    return render(request, 'registration/reset_password_confirm.html', {'form': form})