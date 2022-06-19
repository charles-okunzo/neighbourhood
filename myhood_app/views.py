from urllib import request
from django.shortcuts import render
from django.views.generic import CreateView
from myhood_app.forms import NeighbourhoodCreateForm

from myhood_app.models import Neighbourhood

# Create your views here.


def home(request):
    return render(request, 'index.html')


def dashboard(request):
    neighbourhoods = Neighbourhood.objects.all()
    context = {
        'neighbourhoods':neighbourhoods
    }
    return render(request, 'myhood_app/dashboard.html', context)

def neighbourhood(request):
    context = {}
    return render(request, 'myhood_app/neighbourhood.html', context)


class NeighbourhoodCreateView(CreateView):
    model = Neighbourhood
    form_class = NeighbourhoodCreateForm
    template_name = 'myhood_app/neighbourhood_form.html'
    success_url = '/dashboard'

    def form_valid(self, form):
        form.instance.admin = self.request.user
        self.user_profile = form.instance.id
        return super().form_valid(form)