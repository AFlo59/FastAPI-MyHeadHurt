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

    def __init__(self, *args, **kwargs):
        super(ModelApiForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-field'})

        new_exist_value = self.initial.get('NewExist', None) if self.instance else None
        
        # If NewExist is Existing, set RetainedJob field to 0 and hide it
        if new_exist_value == 'Existing':
            self.fields['RetainedJob'].initial = 0
            self.fields['RetainedJob'].widget = forms.HiddenInput()
            # Also, make sure to clear any data in the RetainedJob field
            self.fields['RetainedJob'].required = False
            self.cleaned_data['RetainedJob'] = 0
        else:
            # If NewExist is not Existing, show the RetainedJob field
            self.fields['RetainedJob'].widget = forms.TextInput()