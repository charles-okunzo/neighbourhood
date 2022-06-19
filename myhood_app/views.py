from urllib import request
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from myhood_app.forms import BizCreateForm, NeighbourhoodCreateForm, PostCreateForm

from myhood_app.models import Neighbourhood, Post

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
    posts = Post.objects.filter(neighbourhood = hood.id).order_by('-created_at')
    context = {
        'hood':hood,
        'posts':posts
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
            post_form.instance.user = request.user
            hood = Neighbourhood.objects.get(pk=pk)
            post_form.instance.neighbourhood = hood
            post_form.save()
            return redirect('neighbourhood', pk=pk)
    context = {
            'post_form':post_form
    }
    return render(request, 'myhood_app/create_post.html', context)

def create_biz(request, pk):
    biz_form = BizCreateForm()
    if request.method == 'POST':
        biz_form = BizCreateForm(request.POST, request.FILES)
        if biz_form.is_valid():
            biz_form.instance.user = request.user
            hood = Neighbourhood.objects.get(pk=pk)
            biz_form.instance.neighbourhood = hood
            biz_form.save()
            return redirect('neighbourhood', pk=pk)
    context = {
            'biz_form':biz_form
    }
    return render(request, 'myhood_app/biz_create.html', context)


def businesses(request, pk):
    context = {}
    return render(request, 'myhood_app/business.html', context)