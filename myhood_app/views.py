from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def dashboard(request):
    context = {}
    return render(request, 'myhood_app/dashboard.html', context)

def neighbourhood(request):
    context = {}
    return render(request, 'myhood_app/neighbourhood.html', context)