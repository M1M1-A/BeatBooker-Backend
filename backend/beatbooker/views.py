from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import BeatbookerSerializer
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse


class UserView(viewsets.ModelViewSet):
    serializer_class = BeatbookerSerializer 
    queryset = User.objects.all()


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponse("Login successful", status=200)
        else:
            return HttpResponse("Login failed", status=401)
