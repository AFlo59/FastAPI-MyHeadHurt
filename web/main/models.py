from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator
import forms

class User(AbstractUser):
    pass

class ModelApi(models.Model):
    US_STATES = [
        ("AL", "Alabama"),
        ("AK", "Alaska"),
        ("AZ", "Arizona"),
        ("AR", "Arkansas"),
        ("CA", "California"),
        ("CO", "Colorado"),
        ("CT", "Connecticut"),
        ("DE", "Delaware"),
        ("FL", "Florida"),
        ("GA", "Georgia"),
        ("HI", "Hawaii"),
        ("ID", "Idaho"),
        ("IL", "Illinois"),
        ("IN", "Indiana"),
        ("IA", "Iowa"),
        ("KS", "Kansas"),
        ("KY", "Kentucky"),
        ("LA", "Louisiana"),
        ("ME", "Maine"),
        ("MD", "Maryland"),
        ("MA", "Massachusetts"),
        ("MI", "Michigan"),
        ("MN", "Minnesota"),
        ("MS", "Mississippi"),
        ("MO", "Missouri"),
        ("MT", "Montana"),
        ("NE", "Nebraska"),
        ("NV", "Nevada"),
        ("NH", "New Hampshire"),
        ("NJ", "New Jersey"),
        ("NM", "New Mexico"),
        ("NY", "New York"),
        ("NC", "North Carolina"),
        ("ND", "North Dakota"),
        ("OH", "Ohio"),
        ("OK", "Oklahoma"),
        ("OR", "Oregon"),
        ("PA", "Pennsylvania"),
        ("RI", "Rhode Island"),
        ("SC", "South Carolina"),
        ("SD", "South Dakota"),
        ("TN", "Tennessee"),
        ("TX", "Texas"),
        ("UT", "Utah"),
        ("VT", "Vermont"),
        ("VA", "Virginia"),
        ("WA", "Washington"),
        ("WV", "West Virginia"),
        ("WI", "Wisconsin"),
        ("WY", "Wyoming"),
    ]

    NAICS_CHOICES = [
    ("11", "Agriculture, forestry, fishing and hunting"),
    ("21", "Mining, quarrying, and oil and gas extraction"),
    ("22", "Utilities"),
    ("23", "Construction"),
    ("31-33", "Manufacturing"),  
    ("42", "Wholesale trade"),
    ("44-45", "Retail trade"),  
    ("48-49", "Transportation and warehousing"), 
    ("51", "Information"),
    ("52", "Finance and insurance"),
    ("53", "Real estate and rental and leasing"),
    ("54", "Professional, scientific, and technical services"),
    ("55", "Management of companies and enterprises"),
    ("56", "Administrative and support and waste management and remediation services"),
    ("61", "Educational services"),
    ("62", "Health care and social assistance"),
    ("71", "Arts, entertainment, and recreation"),
    ("72", "Accommodation and food services"),
    ("81", "Other services (except public administration) 92 Public administration"),
    ]
    
    URBAN_RURAL_CHOICES = [
        ("urban", "Urban"),
        ("rural", "Rural"),
        ("unknown", "Undefined"),
    ]
    REV_LINE_CR_CHOICES = [
        (True, "Yes"),
        (False, "No"),
    ]
    LOW_DOC_CHOICES = [
        (False, "No"),
        (True, "Yes"),
    ]
    FRANCHISE_CHOICES = [
        (0, "No"),
        (1, "Yes"),
    ]

    APPROVAL_YEAR_CHOICES = [(year, str(year)) for year in range(1950, 2025)]

    City = models.CharField(max_length=100)
    State = models.CharField(max_length=2, choices=US_STATES)
    Bank = models.CharField(max_length=100)
    BankState = models.CharField(max_length=2, choices=US_STATES)
    NAICS = models.CharField(max_length=10, choices=NAICS_CHOICES)
    ApprovalDate = models.DateField(input_formats=['%d/%m/%Y'])
    ApprovalFY = models.IntegerField(choices=APPROVAL_YEAR_CHOICES)
    Term = models.IntegerField(min_value=1)
    NoEmp = models.IntegerField(min_value=1)
    NewExist = models.BooleanField(choices=[(True, "New"), (False, "Existing")])
    CreateJob = models.IntegerField(min_value=0)
    RetainedJob = models.IntegerField(min_value=0)
    UrbanRural = models.CharField(max_length=10, choices=URBAN_RURAL_CHOICES)
    RevLineCr = models.BooleanField(choices=REV_LINE_CR_CHOICES)
    LowDoc = models.BooleanField(choices=LOW_DOC_CHOICES)
    GrAppv = models.IntegerField(min_value=0)
    SBA_Appv = models.IntegerField(min_value=0)
    Franchise = models.BooleanField(choices=FRANCHISE_CHOICES)


    def __init__(self, *args, **kwargs):
        super(ModelApi, self).__init__(*args, **kwargs)
        if self.NewExist:  # If NewExist is True (New)
            self.fields['RetainedJob'].widget = forms.HiddenInput()  # Hide
        else:  # If NewExist is False (Existing)
            self.fields['RetainedJob'].widget = forms.TextInput()  # Show
