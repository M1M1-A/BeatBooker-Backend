from django.db import models

class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    
    def _str_(self):
        return self.name