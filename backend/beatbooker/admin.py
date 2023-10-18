from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'firstname', 'lastname')

admin.site.register(UserProfile)
