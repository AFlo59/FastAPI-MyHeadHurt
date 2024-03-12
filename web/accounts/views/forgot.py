# forgot.py
import os
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from mailjet_rest import Client
from django.contrib import messages

from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import views as auth_views

password_reset_confirm = auth_views.PasswordResetConfirmView.as_view()

from accounts.forms import ForgotPasswordForm
from accounts.models import CustomUser


def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = CustomUser.objects.filter(email=email).first()
            if user:
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)
                reset_url = reverse('accounts:password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
                reset_link = request.build_absolute_uri(reset_url)

                mailjet_api_key = os.environ.get('MAILJET_API_KEY')
                mailjet_api_secret = os.environ.get('MAILJET_SECRET_KEY')
                mailjet_sender = os.environ.get('MAILJET_SENDER')

                mailjet = Client(auth=(mailjet_api_key, mailjet_api_secret))
                data = {
                    'FromEmail': mailjet_sender,
                    'FromName': 'Your Site Name',
                    'Subject': 'Password Reset Request',
                    'Html-part': f'Click the link below to reset your password:<br><a href="{reset_link}">{reset_link}</a>',
                    'Recipients': [{
                        'Email': email,
                    }]
                }
                result = mailjet.send.create(data=data)
                if result.status_code == 201:
                    messages.success(request, 'An email with password reset instructions has been sent to your email address.')
                    return redirect('login')
                else:
                    messages.error(request, 'Failed to send password reset email.')
            else:
                messages.error(request, 'No user found with this email address.')
    else:
        form = ForgotPasswordForm()

    return render(request, 'registration/forgot_password.html', {'form': form})

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