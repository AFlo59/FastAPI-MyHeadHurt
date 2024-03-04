import os
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .forms import RegisterForm
from .models import CustomUser  # Import your CustomUser model here
from mailjet_rest import Client

UserModel = get_user_model()  # No argument needed

class LoginView(auth_views.LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    
@login_required
def username_page(request, username):
    return render(request, 'registration/username.html', {'username': username})

@login_required
def custom_logout(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', 'home'))

class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('home')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save(commit=False)
        user.is_active = False  # Do not activate the account immediately
        user.save()
        self.send_confirmation_email(user)
        return response

    def send_confirmation_email(self, user):
        # Construct the email content
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
                    "HTMLPart": f"<h3>Dear {user.username}, welcome to our website!</h3>"
                                "<br />Please click the following link to activate your account:"
                                f"<br /><a href='{self.get_activation_link(user)}'>Activate account</a>",
                }
            ]
        }

        # Send the email using Mailjet API
        api_key = os.getenv('MAILJET_API_KEY')
        api_secret = os.getenv('MAILJET_SECRET_KEY')
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        mailjet.send.create(data=data)

    def get_activation_link(self, user):
        # Construct the activation link
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        return reverse('accounts:validate_email', kwargs={'uidb64': uidb64, 'token': token})

    def get_success_url(self):
        # Set is_active to True before redirection
        self.object.is_active = True
        self.object.save()
        return reverse_lazy('accounts:username', kwargs={'username': self.object.username})

class ValidateEmailView(View):
    def get(self, request, uidb64, token):
        try:
            uid = str(urlsafe_base64_decode(uidb64), 'utf-8')
            user = UserModel.objects.get(pk=uid)

            if default_token_generator.check_token(user, token):
                user.is_active = True
                user.save()
                return redirect('account_activation_success')
            else:
                return render(request, 'registration/activation_link_invalid.html')
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            return render(request, 'registration/activation_link_invalid.html')