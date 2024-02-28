from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .models import CustomUser

class UserCreationFormCustom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser

class SignUpView(CreateView):
    form_class = UserCreationFormCustom
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def username_page(request, username):
    return render(request, 'accounts/username.html', {'username': username})

@login_required
def profil_page(request):
    return render(request, "accounts/profil_page.html")

def custom_logout(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', 'home'))
