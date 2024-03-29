from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.forms.widgets import TextInput
from django.core.validators import RegexValidator
from django.utils import timezone
import datetime

user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# Create your models here.
class Functionalities(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    
    def __str__(self):
        return f'{self.name} : {self.description}'
    
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


    City = models.CharField(max_length=100)
    State = models.CharField(max_length=2, choices=US_STATES)
    Bank = models.CharField(max_length=100)
    BankState = models.CharField(max_length=2, choices=US_STATES)
    NAICS = models.CharField(max_length=10, choices=NAICS_CHOICES)
    Term = models.IntegerField(validators=[MinValueValidator(1)])
    NoEmp = models.IntegerField(validators=[MinValueValidator(1)])
    NewExist = models.BooleanField(choices=[(True, "New"), (False, "Existing")])
    CreateJob = models.IntegerField(validators=[MinValueValidator(0)])
    RetainedJob = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null=True)
    UrbanRural = models.CharField(max_length=10, choices=URBAN_RURAL_CHOICES)
    RevLineCr = models.BooleanField(choices=REV_LINE_CR_CHOICES)
    LowDoc = models.BooleanField(choices=LOW_DOC_CHOICES)
    GrAppv = models.IntegerField(validators=[MinValueValidator(0)])
    SBA_Appv = models.IntegerField(validators=[MinValueValidator(0)])
    Franchise = models.BooleanField(choices=FRANCHISE_CHOICES)
