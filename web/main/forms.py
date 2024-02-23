from django import forms 
from .models import CryptoApi,ModelApi

class CryptoApiForm(forms.ModelForm):
    class Meta:
        model = CryptoApi
        fields = "__all__"
        labels = {
            'slug' : 'Entrez votre crypto ici',
            'convert' : 'Entrez votre devise ici'
        }

class ModelApiForm(forms.ModelForm):
    class Meta:
        model = ModelApi
        fields = "__all__"
