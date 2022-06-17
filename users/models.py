from django.db import models
from django.contrib.auth.models import AbstractUser

from myhood_app.models import Neighbourhood

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100, null=True, blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, related_name='user', on_delete=models.CASCADE, null=True)