from django.urls import path
from .views import *



urlpatterns = [

path('register/', Register.as_view(), name='register'),
path('signin/', Signin.as_view(), name='signin'),
path('logout/', LogoutView.as_view(), name='logout'),
path('', home, name = 'home' ),


]