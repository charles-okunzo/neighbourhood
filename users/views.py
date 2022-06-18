from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User

from users.forms import UserRegisterForm

# Create your views here.

class Register(CreateView):
    model = User
    form_class = UserRegisterForm