from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import ModelApiForm
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
from django.contrib.auth.forms import AuthenticationForm


def news_page(request):
    return render(request, 'main/news_page.html')

def home_page(request):
    return render(request, 'main/home_page.html')

def about_page(request):
    return render(request, 'main/about_page.html')

def contact_page(request, test):
    context = {'test': test}
    return render(request, 'main/contact_page.html', context=context)

