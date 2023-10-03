from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
from rest_framework import viewsets
from .serializers import BeatbookerSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token
from django.db import IntegrityError
import json

def signup_view(request):
    json_string = request.body.decode('utf-8')
    data = json.loads(json_string)
    print("DATA", data)

    if request.method == 'POST':
        username = data['username']
        password = data['password']
        email = data['email']
        firstname = data['firstname']
        lastname = data['lastname']

    if username and password and email:
        try:
            new_user = User.objects.create_user(username, email, password)
        except IntegrityError:
            return HttpResponse("User already Exists", status=201)
        else:
            new_user.first_name = firstname
            new_user.last_name = lastname
            new_user.save()
            return HttpResponse("User Created successful", status=200)       
    else:
        return HttpResponse("SignUp failed", status=401)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponse("Login successful", status=200)
        else:
            return HttpResponse("Login failed", status=401)

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})

