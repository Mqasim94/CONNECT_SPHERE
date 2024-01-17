from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import CreateView
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import Register_Form
# Create your views here.

# class Register(CreateView):
#     model = User
#     template_name = 'users/register.html'
#     form = UserCreationForm
#     success_url = '/users/signin/'

def register_page(request):
    form = Register_Form()
    if request.method == 'POST':
        form = Register_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        
    else:
        form = Register_Form()

    return render(request, 'users/register.html', {'form':form})

def signin (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate (request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse ("loged In")        
        else: 
            messages.error(request, "Try Again!, 'Username' and 'Password' is incorrect")

    context = {}
    return render(request, 'users/signin.html', context)

def home(request):

    return render(request, 'users/home.html')
    