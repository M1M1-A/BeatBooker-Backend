from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
from rest_framework import viewsets
from .serializers import BeatbookerSerializer
#from .models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token

# class UserView(viewsets.ModelViewSet):
#     serializer_class = BeatbookerSerializer
#     queryset = User.objects.all()

def login_view(request):

    user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")

    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        print(form)
        print(request.POST)
        # print(form.is_valid())
        # print("FORM", form.errors)

        if form.is_valid():
            username = request.POST.get('username')
            password = form.cleaned_data.get('password')

            print("USERNAME", username)
            print("PASSWORD", password)
            
            user = authenticate(request, username=username, password=password)
            print("USER",user)

            if user is not None:
                login(request, user)
                return HttpResponse("Login successful", status=200)
        else:
            return HttpResponse("Login failed", status=401)

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})