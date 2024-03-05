import os
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import RegisterForm
from .models import CustomUser
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
class ResendActivationEmailView(View):
    def get(self, request, *args, **kwargs):
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')
        user = get_object_or_404(CustomUser, pk=uidb64)

        if default_token_generator.check_token(user, token):
            # Send activation email
            RegisterView().send_confirmation_email(user)
            return HttpResponse("Activation email has been resent successfully.")
        else:
            return HttpResponse("Invalid activation token.")

    def post(self, request, *args, **kwargs):
        # Handle POST requests here
        # Example code to handle POST request and resend activation email
        uidb64 = request.POST.get('uidb64')
        token = request.POST.get('token')
        user = get_object_or_404(CustomUser, pk=uidb64)

        if default_token_generator.check_token(user, token):
            # Send activation email
            RegisterView().send_confirmation_email(user)
            return HttpResponse("Activation email has been resent successfully.")
        else:
            return HttpResponse("Invalid activation token.")

class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('home')
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
