from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import CreateView, View
from .models import User
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import Register_Form, Signin_Form
# Create your views here.

# class Register(CreateView):
#     model = User
#     template_name = 'users/register.html'
#     form = UserCreationForm
#     success_url = '/users/signin/'

# def register_page(request):
#     form = Register_Form()
#     if request.method == 'POST':
#         form = Register_Form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('signin')
        
#     else:
#         form = Register_Form()

#     return render(request, 'users/register.html', {'form':form})

class Register(CreateView):
    model = User
    form_class = Register_Form
    template_name = 'users/register.html'
    success_url = '/users/signin/'


class Signin(View):
    template_name = 'users/signin.html'
    form_class = Signin_Form
    # success_url = reverse_lazy('post_list')
    
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
            if user is not None:
                login(request, user)
                # return redirect('posts/List_Post')
                return HttpResponse('logged in')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})
    
class LogoutView(LogoutView):

    success_url= '/users/home.html'



# def signin (request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate (request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return HttpResponse ("loged In")        
#         else: 
#             messages.error(request, "Try Again!, 'Username' and 'Password' is incorrect")

#     context = {}
#     return render(request, 'users/signin.html', context)

def home(request):

    return render(request, 'users/home.html')
    