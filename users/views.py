from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import CreateView, View
from .models import User
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import Register_Form, Signin_Form



class Register(CreateView):
    model = User
    form_class = Register_Form
    template_name = 'users/register.html'
    success_url = '/signin/'


class Signin(View):
    template_name = 'users/signin.html'
    form_class = Signin_Form
    success_url = '/posts/post_list/'
    
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
    

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user:
                login(request, user)
                return redirect('/posts/List_Post/')
            else:
                return HttpResponse('wrong Credentials')
        
        



def home(request):

    return render(request, 'users/home.html')
    