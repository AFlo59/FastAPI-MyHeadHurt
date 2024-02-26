from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import ModelApiForm
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os

def custom_logout(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', 'home'))

# Create your views here.
def home_page(request):
    return render(request, 'main/home_page.html')

def about_page(request):
    return render(request, 'main/about_page.html')

def contact_page(request, test):
    context = {'test': test}
    return render(request, 'main/contact_page.html', context=context)

@login_required
def profil_page(request):
    return render(request, "main/profil_page.html")

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

            return render(request, "main/predict_page.html", context={'form':form, 'data': data})

    else:
        form = ModelApiForm()

    
    return render(request, "main/predict_page.html", context={'form':form})