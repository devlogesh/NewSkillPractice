from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        exclude = ['user_id']