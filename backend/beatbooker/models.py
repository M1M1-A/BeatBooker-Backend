from django.db import models
from django.core.exceptions import ValidationError

class User(models.Model):
    username = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)

    def _str_(self):
        return self.username
