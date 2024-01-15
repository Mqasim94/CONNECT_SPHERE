from django.shortcuts import render, render, HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView, ListView
from .models import Profile
# from .forms import Profile_Model_Form

class profile_Create(CreateView):
    model = Profile
    fields = '__all__'
    template_name = 'posts/profile.html'  

class Detail_profile(DetailView):
    model = Profile
    template_name= 'posts/detail_profile.html'
 
class List_profile(ListView):
    model = Profile
    feilds = '__all__'
    template_name = 'posts/List_profile.html' 

class Update_Profile(UpdateView):
    model = Profile
    fields = '__all__'
    template_name = 'posts/update_profile.html'
    success_url = '/posts/List_profile/'

class Delet_profile(DetailView):
    model = Profile
    template_name = 'posts/delet_profile.html'
    success_url = '/posts/List_profile/'
