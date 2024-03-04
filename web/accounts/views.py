from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, View
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from mailjet_rest import Client
from .models import CustomUser  # Import your CustomUser model here
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
        
        # Generate and send validation email
        self.send_validation_email(user)
        
        return response

    def send_validation_email(self, user):
        # Generate a unique validation token
        token = default_token_generator.make_token(user)
        
        # Build the validation link
        current_site = get_current_site(self.request)
        validation_url = reverse('validate_email', kwargs={'uidb64': urlsafe_base64_encode(force_bytes(user.pk)), 'token': token})
        validation_link = f"{settings.BASE_URL}{validation_url}"
        
        # Construct the email content
        subject = "Activate Your Account"
        message = render_to_string('registration/validation_email.html', {
            'user': user,
            'validation_link': validation_link,
            'domain': current_site.domain,
        })
        
        # Send the email
        email = EmailMessage(subject, message, to=[user.email])
        email.send()

    def get_success_url(self):
        # Redirect to the user's profile page
        return reverse('accounts:username', kwargs={'username': self.object.username})


class ValidateEmailView(View):
    def get(self, request, uidb64, token):
        try:
            # Decode user ID and get the user
            uid = str(urlsafe_base64_decode(uidb64), 'utf-8')
            user = CustomUser.objects.get(pk=uid)  # Use CustomUser model here
            
            # Validate the token
            if default_token_generator.check_token(user, token):
                # Activate the user's account
                user.is_active = True
                user.save()
                # Redirect to success page
                return redirect('account_activation_success')
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):  # Use CustomUser model here
            pass
        # Redirect to invalid token page
        return redirect('account_activation_invalid')