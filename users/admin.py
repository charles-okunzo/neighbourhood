from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, User
# Register your models here.

admin.site.register(Profile)