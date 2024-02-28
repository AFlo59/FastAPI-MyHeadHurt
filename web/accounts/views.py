from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render

from .forms import LoginForm, RegisterForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


def accounts_page(request, username):
    # Assuming you have a template named username.html
    return render(request, 'accounts/username.html', {'username': username})