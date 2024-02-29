from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from .forms import *
from mailjet_rest import Client
import os

class LoginView(auth_views.LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    
@login_required
def username_page(request, username):
    return render(request, 'registration/username.html', {'username': username})


def custom_logout(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', 'home'))


api_key = os.environ.get('MAILJET_API')
api_secret = os.environ.get('MAILJET_SECRET')
mailjet = Client(auth=(api_key, api_secret), version='v3.1')

class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save(commit=False)
        user.is_active = False  # Do not activate the account immediately
        user.save()
        self.send_confirmation_email(user)
        return response

    def send_confirmation_email(self, user):
        # Construct the email data
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": "etudessup59230@gmail.com",
                        "Name": "Florian"
                    },
                    "To": [
                        {
                            "Email": user.email,
                            "Name": user.username  # You can customize this if needed
                        }
                    ],
                    "Subject": "Welcome to Our Website",
                    "TextPart": f"Dear {user.username}, welcome to our website!",
                    "HTMLPart": f"<h3>Dear {user.username}, welcome to our website!</h3><br />We're excited to have you onboard!",
                    "CustomID": "RegistrationConfirmation"
                }
            ]
        }
        # Send the email
        mailjet.send.create(data=data)

    def get_success_url(self):
        # Redirect to the user's profile page
        return reverse('accounts:username', kwargs={'username': self.object.username})
