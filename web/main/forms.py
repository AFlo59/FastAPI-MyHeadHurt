from django import forms 
from .models import *
class ModelApiForm(forms.ModelForm):
    ApprovalDate = forms.DateField(label='Veuillez entrer la date SBA commitment issued', widget=DateInput())

    class Meta:
        model = ModelApi
        fields = "__all__"
        labels = {
            'City': 'Veuillez indiquer la ville de l\'emprunteur',
            'State': 'Veuillez indiquer l\'état de l\'emprunteur',
            'Bank': 'Veuillez indiquer le nom de la banque',
            'BankState': 'Veuillez indiquer l\'état de la banque',
            'NAICS': 'Veuillez indiquer la catégorie NAICS',
            'ApprovalFY': 'Veuillez indiquer l\'année fiscale d\'engagement',
            'Term': 'Veuillez indiquer la durée du prêt en mois',
            'NoEmp': 'Veuillez indiquer le nombre d\'employés de l\'entreprise',
            'NewExist': 'Veuillez indiquer si l\'entreprise existe déjà',
            'CreateJob': 'Veuillez indiquer le nombre d\'emplois créés',
            'RetainedJob': 'Veuillez indiquer le nombre d\'emplois maintenus',
            'FranchiseCode': 'Veuillez indiquer si l\'entreprise est franchisée',
            'UrbanRural': 'Veuillez indiquer le type de zone',
            'RevLineCr': 'Veuillez indiquer s\'il existe une ligne de crédit renouvelable',
            'LowDoc': 'Veuillez indiquer si le prêt est un LowDoc Loan',
            'GrAppv': 'Veuillez indiquer le montant brut du prêt approuvé par la banque',
            'SBA_Appv': 'Veuillez indiquer le montant approuvé garanti par la SBA',
        }

    def __init__(self, *args, **kwargs):
        super(ModelApiForm, self).__init__(*args, **kwargs)
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