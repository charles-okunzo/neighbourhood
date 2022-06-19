from django.shortcuts import redirect, render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from users.forms import CustomUserLoginForm, ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

class Register(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'


class UserLogin(LoginView):
    model = User
    form_class = CustomUserLoginForm
    template_name = 'users/login.html'

@login_required
def update_profile(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile_update.html', context)


@login_required
def profile(request):
    context ={}
    return render(request, 'users/profile.html', context)