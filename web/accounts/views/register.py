from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from accounts.forms import RegisterForm
from accounts.models import CustomUser
from accounts.utils import send_confirmation_email

class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)

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

        # Proceed with registration
        user = form.save(commit=False)
        user.is_active = True #False
        user.save()
        send_confirmation_email(request=self.request, user=user)  # Pass the request argument

        messages.success(self.request, 'Account created successfully. Please verify your email.')
        return response

    def get_success_url(self):
        # Set is_active to True before redirection
        self.object.is_active = True
        self.object.save()
        return reverse_lazy('accounts:username', kwargs={'username': self.object.username})