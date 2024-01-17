from django.shortcuts import render, render, HttpResponse
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from django.views.generic import ListView, DetailView
from .models import Profile, Post
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


class Creat_Post(CreateView):
    model = Post
    template_name = 'posts/creat_post.html'
    fields = ['title', 'content', 'created_on', 'image', 'is_private']
    
    success_url = '/posts/List_Post/'

class Update_post(UpdateView):
    model = Post
    fields = ['title', 'content', 'created_on', 'image', 'is_private']
    template_name = 'posts/update_post.html'

class Delet_post(DeleteView):
    model = Post
    template_name = 'posts/delet_post.html'
    success_url = '/posts/List_Post/'


class List_Post(ListView):
    model = Post
    template_name = 'posts/List_post.html'