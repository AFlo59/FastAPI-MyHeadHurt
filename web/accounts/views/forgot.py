import os
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from mailjet_rest import Client

from accounts.forms import ForgotPasswordForm
from accounts.models import CustomUser

def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = CustomUser.objects.filter(email=email).first()
            if user:
                current_site = get_current_site(request)
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)
                reset_url = reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
                reset_link = f'{current_site.domain}{reset_url}'

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