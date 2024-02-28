from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
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