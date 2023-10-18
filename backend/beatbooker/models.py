from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.ImageField()
    genres = models.JSONField()
    hourly_rate = models.DecimalField(max_digits= 8, decimal_places=2)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return str(self.user)
    