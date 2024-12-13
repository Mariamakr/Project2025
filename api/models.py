from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator,DomainNameValidator,MaxValueValidator, MaxLengthValidator,FileExtensionValidator

# Create your models here.
class Team(models.Model):
    TEAM_CHOICES = {
        "SERVICE_DESK": "Service Desk",
        "CLOUD_OPERATIONS": "Cloud Operations",
        "NETWORK_OPERATIONS": "Network Operations",
        "AMS": "AMS",
        "ADS": "ADS"


    }
    name: models.CharField(max_length=30, choices=TEAM_CHOICES.values())

# class Achievements(models.Model):
#     team = models.ForeignKey(Team)
# emotional_exhaustement = "find type for this field"
# physically_exhaustement = "Same here"