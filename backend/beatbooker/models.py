from django.db import models
from django.core.exceptions import ValidationError

class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name
