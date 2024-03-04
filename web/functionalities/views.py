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
    url = 'http://172.17.0.3:8001/predict'

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

    else:
        form = ModelApiForm()

    
    return render(request, "functionalities/predict_page.html", context={'form':form})