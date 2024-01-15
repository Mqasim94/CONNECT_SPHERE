
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [

#path('register/', Register, name = 'register')
path('profile/', profile_Create.as_view(), name='profile'),
path('List_profile/',  List_profile.as_view(), name=' List_profile'),
path('Detail_profile/<pk>/', Detail_profile.as_view(), name='Detail_profile'),


]
        

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)