from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

from myhood_app.models import Neighbourhood

# Create your models here.

# class User(AbstractUser):
#     name = models.CharField(max_length=100, null=True, blank=True)
#     neighbourhood = models.ForeignKey(Neighbourhood, related_name='user', on_delete=models.CASCADE, null=True)

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to = 'profiles', null = True)
    my_location = models.CharField(verbose_name='Location', max_length=100, null=True, blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, related_name='user_profile', on_delete=models.CASCADE, null=True, blank=True)