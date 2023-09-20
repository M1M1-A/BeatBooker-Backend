from django.shortcuts import render

from rest_framework import viewsets
from .serializers import BeatbookerSerializer
from .models import User

class UserView(viewsets.ModelViewSet):
    serializer_class = BeatbookerSerializer
    queryset = User.objects.all()