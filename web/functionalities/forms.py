from django import forms
from .models import *

class ModelApiForm(forms.ModelForm):
    class Meta:
        model = ModelApi
        fields = "__all__"
        labels = {
        'City': 'Please indicate the borrower\'s city',
        'State': 'Please indicate the borrower\'s state',
        'Bank': 'Please indicate the bank\'s name',
        'BankState': 'Please indicate the bank\'s state',
        'NAICS': 'Please indicate the NAICS category',
        'Term': 'Please indicate the loan term in months',
        'NoEmp': 'Please indicate the number of employees of the business',
        'NewExist': 'Please indicate if the business already exists',
        'CreateJob': 'Please indicate the number of jobs created',
        'RetainedJob': 'Please indicate the number of jobs retained',
        'Franchise': 'Please indicate if the business is a franchise',
        'UrbanRural': 'Please indicate the type of area',
        'RevLineCr': 'Please indicate if there is a revolving line of credit',
        'LowDoc': 'Please indicate if the loan is a LowDoc Loan',
        'GrAppv': 'Please indicate the gross amount of the loan approved by the bank',
        'SBA_Appv': 'Please indicate the amount guaranteed approved by the SBA',
    }
    
    widgets = {
            'City': forms.TextInput(attrs={'class': 'form-field', 'required': True}),
            'State': forms.Select(attrs={'class': 'form-field', 'required': True}),
            'Bank': forms.TextInput(attrs={'class': 'form-field', 'required': True}),
            'BankState': forms.Select(attrs={'class': 'form-field', 'required': True}),
            'NAICS': forms.Select(attrs={'class': 'form-field', 'required': True}),
            'Term': forms.NumberInput(attrs={'class': 'form-field', 'required': True, 'min': 1}),
            'NoEmp': forms.NumberInput(attrs={'class': 'form-field', 'required': True, 'min': 1}),
            'NewExist': forms.Select(attrs={'class': 'form-field', 'required': True}),
            'CreateJob': forms.NumberInput(attrs={'class': 'form-field', 'required': True, 'min': 0}),
            'RetainedJob': forms.NumberInput(attrs={'class': 'form-field', 'required': False, 'min': 0}),
            'Franchise': forms.Select(attrs={'class': 'form-field', 'required': True}),
            'UrbanRural': forms.Select(attrs={'class': 'form-field', 'required': True}),
            'RevLineCr': forms.Select(attrs={'class': 'form-field', 'required': True}),
            'LowDoc': forms.Select(attrs={'class': 'form-field', 'required': True}),
            'GrAppv': forms.NumberInput(attrs={'class': 'form-field', 'required': True, 'min': 0}),
            'SBA_Appv': forms.NumberInput(attrs={'class': 'form-field', 'required': True, 'min': 0}),
        }

    def __init__(self, *args, **kwargs):
        super(ModelApiForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-field'})