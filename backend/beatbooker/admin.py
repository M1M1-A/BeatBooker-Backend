from django.contrib import admin
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'firstname', 'lastname')

admin.site.register(User, UserAdmin)