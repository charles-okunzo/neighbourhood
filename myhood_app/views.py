from urllib import request
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from myhood_app.forms import BizCreateForm, NeighbourhoodCreateForm, PostCreateForm
from django.contrib.auth.decorators import login_required

from myhood_app.models import Business, Neighbourhood, Post

# Create your views here.


def home(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    if request.method == 'POST':
        print(request.POST.get('hood-id'))
    neighbourhoods = Neighbourhood.objects.all()
    context = {
        'neighbourhoods':neighbourhoods
    }
    return render(request, 'myhood_app/dashboard.html', context)

def join_hood(request, pk):
    neighbourhood = Neighbourhood.objects.get(pk=pk)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('dashboard')

def leave_hood(request, pk):
    neighbourhood = Neighbourhood.objects.get(pk=pk)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('dashboard')

@login_required
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
@login_required
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
@login_required
def create_biz(request, pk):
    biz_form = BizCreateForm()
    if request.method == 'POST':
        biz_form = BizCreateForm(request.POST, request.FILES)
        if biz_form.is_valid():
            biz_form.instance.user = request.user
            hood = Neighbourhood.objects.get(pk=pk)
            biz_form.instance.neighbourhood = hood
            biz_form.save()
            return redirect('biz-page', pk=pk)
    context = {
            'biz_form':biz_form
    }
    return render(request, 'myhood_app/biz_create.html', context)

@login_required
def businesses(request, pk):
    hood = Neighbourhood.objects.get(pk=pk)
    businesses = Business.objects.filter(neighbourhood = hood)

    if 'biz_name' in request.GET and request.GET.get('biz_name'):
        search_term = request.GET.get('biz_name')
        businesses = Business.find_business(search_term)
        message = f'{search_term}'
        hood = Neighbourhood.objects.get(pk=pk)
        found_biz = businesses
        # businesses = Business.objects.filter(neighbourhood = hood)
        context = {
            'hood':hood,
            'businesses':businesses,
            'message':message,
            'found_biz':found_biz
        }
        return render(request, 'myhood_app/search_biz.html', context)
    else:
        hood = Neighbourhood.objects.get(pk=pk)
        businesses = Business.objects.filter(neighbourhood = hood)
        context = {
            'hood':hood,
            'businesses':businesses
        }
        return render(request, 'myhood_app/business.html', context)