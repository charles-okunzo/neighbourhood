from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('neighbourhood/<int:pk>', views.neighbourhood, name = 'neighbourhood'),
    path('create/neighbourhood', views.NeighbourhoodCreateView.as_view(), name='create-hood'),
    path('neighbourhood/post/new/<int:pk>', views.neighbourhood, name = 'hood-post'),

]
