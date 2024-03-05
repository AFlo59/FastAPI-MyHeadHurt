import os
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import CreateView
from mailjet_rest import Client

from accounts.forms import RegisterForm
from accounts.models import CustomUser

class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        # Check if email or username is already in use
        email = form.cleaned_data['email']
        username = form.cleaned_data['username']
        existing_user = CustomUser.objects.filter(email=email, is_active=False).first() or CustomUser.objects.filter(username=username, is_active=False).first()
        if existing_user:
            messages.error(self.request, 'An account with the same username and email already exists but is not active.')
            return self.form_invalid(form)

        # Check if passwords match
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']
        if password1 != password2:
            messages.error(self.request, 'Passwords do not match.')
            return self.form_invalid(form)

        # Check password complexity (you can define your own criteria)
        if len(password1) < 8:
            messages.error(self.request, 'Password must be at least 8 characters long.')
            return self.form_invalid(form)

        # If all checks pass, proceed with registration
        response = super().form_valid(form)
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        self.send_confirmation_email(user)
        messages.success(self.request, 'Account created successfully. Please verify your email.')
        return response

    def send_confirmation_email(self, user):
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        activation_link = reverse('accounts:validate_email', kwargs={'uidb64': uidb64, 'token': token})
        
        # Construct the email content
        email_content = f"<h3>Dear {user.username}, welcome to our website!</h3>" \
                        f"<br />Please click the following link to activate your account:" \
                        f"<br /><a href='{activation_link}'>Activate account</a>"

        # Construct the Mailjet email data
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": "etudessup59230@gmail.com",
                        "Name": "Admin"
                    },
                    "To": [
                        {
                            "Email": user.email,
                            "Name": user.username
                        }
                    ],
                    "Subject": "Email validation",
                    "HTMLPart": email_content,
                }
            ]
        }

        # Send the email using Mailjet API
        api_key = os.getenv('MAILJET_API_KEY')
        api_secret = os.getenv('MAILJET_SECRET_KEY')
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        mailjet.send.create(data=data)
        
    def get_success_url(self):
        # Set is_active to True before redirection
        self.object.is_active = True
        self.object.save()
        return reverse_lazy('accounts:username', kwargs={'username': self.object.username})
