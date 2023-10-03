from rest_framework import serializers
from .models import User

class BeatbookerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'firstname', 'lastname')
