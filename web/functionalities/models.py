from django.db import models

# Create your models here.
class Functionalities(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    
    def __str__(self):
        return f'{self.name} : {self.description}'