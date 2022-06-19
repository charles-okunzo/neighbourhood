from urllib import request
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from myhood_app.forms import NeighbourhoodCreateForm, PostCreateForm

from myhood_app.models import Neighbourhood

# Create your views here.


def home(request):
    return render(request, 'index.html')


def dashboard(request):
    if request.method == 'POST':
        print(request.POST.get('hood-id'))
    neighbourhoods = Neighbourhood.objects.all()
    context = {
        'neighbourhoods':neighbourhoods
    }
    return render(request, 'myhood_app/dashboard.html', context)



def neighbourhood(request, pk):
    hood = Neighbourhood.objects.get(pk=pk)
    context = {
        'hood':hood
    }
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

def create_post(request, pk):
    post_form = PostCreateForm()
    if request.method == 'POST':
        post_form = PostCreateForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            return redirect('neighbourhood', pk=pk)
    context = {

    }
    return render(request, 'my_hood_app/create_post.html', context)