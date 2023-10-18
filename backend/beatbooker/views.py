from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token
from django.db import IntegrityError
import json
from .models import UserProfile

def signup_view(request):
    json_string = request.body.decode('utf-8')
    data = json.loads(json_string)

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
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponse("Login successful", status=200)
        else:
            return HttpResponse("Login failed", status=401)

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})

def update_profile_view(request):
    json_string = request.body.decode('utf-8')
    data = json.loads(json_string)

    if request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            profile = UserProfile.objects.get_or_create(user=user)[0]
            profile.user = data['user']
            profile.name = data['name']
            profile.bio = data['bio']
            profile.image = data['image']
            profile.genres = data['genres']
            profile.hourly_rate = data['hourly_rate']
            profile.phone = data['phone']
            profile.save()
            return HttpResponse("Profile Created successful", status=201)
        else:
            return HttpResponse("User not authenticated", status=401)



