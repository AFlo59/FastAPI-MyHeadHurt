import os
from django.shortcuts import render
from .models import Functionalities
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required  
from .forms import ModelApiForm  
import json
<<<<<<< HEAD
import os
from requests import Session
=======
from requests import Session, Timeout, TooManyRedirects
from json import JSONDecodeError
>>>>>>> efdc92fe11a7a189cd7006dedc1bab6197657122


class FunctionalitiesListView(LoginRequiredMixin, ListView):
    model = Functionalities
    template_name = "functionalities/funct_list.html"


class FunctionalitiesDetailView(DetailView):
    model = Functionalities
    template_name = "functionalities/funct_detail.html"

@login_required
def predict_page(request):
<<<<<<< HEAD
    url = os.getenv('API_URL')

    headers = {
    'Accepts': 'application/json',
    }

    session = Session()
    session.headers.update(headers)

        # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ModelApiForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)
            
            features = json.dumps(form.cleaned_data)
            response = session.post(url, data=features)
            data = json.loads(response.text)
            form.save()
            print('ok')

            return render(request, "functionalities/predict_page.html", context={'form':form, 'data': data})

=======
    if request.user.is_authenticated:
        # Retrieve user information if user is logged in
        user_info = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'date_of_birth': request.user.date_of_birth,
            'phone_number': request.user.phone_number,
        }
        # Initialize form with user information
        form = ModelApiForm(initial=user_info)
>>>>>>> efdc92fe11a7a189cd7006dedc1bab6197657122
    else:
        form = ModelApiForm()

    api_url = os.environ.get('URL_API')#"http://api:8001/funct/predict/"

    if request.method == "POST":
        form = ModelApiForm(request.POST)
        if form.is_valid():
            try:
                headers = {'Content-Type': 'application/json'}
                # Serialize form data to JSON
                data_input = json.dumps(form.cleaned_data)
                with Session() as session:
                    response = session.post(api_url, data=data_input, headers=headers)
                    data = response.json()
                form.save()
                return render(request, "functionalities/predict_page.html", context={"form": form, "data": data})
            except (ConnectionError, Timeout, TooManyRedirects, KeyError, JSONDecodeError) as e:
                return render(request, "functionalities/predict_page.html", context={"form": form, "error": e})
        else:
            return render(request, "functionalities/predict_page.html", context={"form": form})

    return render(request, "functionalities/predict_page.html", context={"form": form})