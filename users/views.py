from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from users.forms import CustomUserLoginForm, UserRegisterForm

# Create your views here.

class Register(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'


class UserLogin(LoginView):
    model = User
    form_class = CustomUserLoginForm
    template_name = 'users/login.html'

def profile(request):
    context ={}
    return render(request, 'users/profile.html', context)