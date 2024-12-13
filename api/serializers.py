from rest_framework import serializers
# from .models import Team, Achievements
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token