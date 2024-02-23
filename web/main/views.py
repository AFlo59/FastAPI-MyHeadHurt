from django.shortcuts import render
from .utils import mutliplicate_by_5
from django.contrib.auth.decorators import login_required
from .forms import CryptoApiForm, ModelApiForm
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os

@login_required
def api_page(request):
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.getenv('API_KEY'),
    }

    session = Session()
    session.headers.update(headers)

        # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = CryptoApiForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            try :
                response = session.get(url, params=form.cleaned_data)
                data = json.loads(response.text)
                print(form.cleaned_data)
                form.save()
                id_ = list(data['data'].keys())[0]
                print(id_)
                devise = form.cleaned_data['convert']
                data = data['data'][id_]['quote'][devise]

                return render(request, "main/api_page.html", context={'form':form, 'data': data, 'devise':devise})
            except (ConnectionError, Timeout, TooManyRedirects, KeyError) as e:
                return render(request, "main/api_page.html", context={'form':form, 'error':e})
    else:
        form = CryptoApiForm()

    
    return render(request, "main/api_page.html", context={'form':form})



# Create your views here.
def home_page(request):
    return render(request, 'main/home_page.html')

def about_page(request):
    return render(request, 'main/about_page.html')

def contact_page(request, test):
    context = {'test': test}
    return render(request, 'main/contact_page.html', context=context)

@login_required
def special_page(request):
    return render(request, "main/special_page.html")



@login_required
def api_predict_page(request):
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

            return render(request, "main/api_predict_page.html", context={'form':form, 'data': data})

    else:
        form = ModelApiForm()

    
    return render(request, "main/api_predict_page.html", context={'form':form})