import os
from django.shortcuts import render
from .models import Functionalities
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required  # Import login_required decorator
from .forms import ModelApiForm  # Import your ModelApiForm
import json
from requests import Session


class FunctionalitiesListView(LoginRequiredMixin, ListView):
    model = Functionalities
    template_name = "functionalities/funct_list.html"


class FunctionalitiesDetailView(DetailView):
    model = Functionalities
    template_name = "functionalities/funct_detail.html"

@login_required
def predict_page(request):
    url = os.environ.get('URL_API')

    headers = {
        'Accepts': 'application/json',
    }

    session = Session()
    session.headers.update(headers)

    # Vérifie si l'utilisateur est connecté
    if request.user.is_authenticated:
        # Récupère les informations de l'utilisateur connecté
        user_info = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'date_of_birth': request.user.date_of_birth,
            'phone_number': request.user.phone_number,
        }
        # Crée une instance de formulaire pré-remplie avec les informations de l'utilisateur
        form = ModelApiForm(initial=user_info)
    else:
        form = ModelApiForm()

    # Si la requête est POST, traite les données du formulaire
    if request.method == "POST":
        form = ModelApiForm(request.POST)
        if form.is_valid():
            features = json.dumps(form.cleaned_data)
            response = session.post(url, data=features)
            data = json.loads(response.text)
            form.save()
            print('ok')
            return render(request, "functionalities/predict_page.html", context={'form': form, 'data': data})

    return render(request, "functionalities/predict_page.html", context={'form': form})