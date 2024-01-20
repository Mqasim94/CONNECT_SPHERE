
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'posts'

urlpatterns = [

#path('register/', Register, name = 'register')
path('profile/', profile_Create.as_view(), name='profile'),
path('UserProfile/', UserProfile, name='UserProfile'),
path('List_profile/',  List_profile.as_view(), name=' List_profile'),
path('Detail_profile/<pk>/', Detail_profile.as_view(), name='Detail_profile'),
path('Delet_profile/<pk>/',  Delet_profile.as_view(), name=' Delet_profile'),
path('Update_Profile/<pk>/', Update_Profile.as_view(), name='Update_Profile'),
path('UserPost/<pk>/', UserPost.as_view(), name='UserPost'),


path('Creat_Post/', Creat_Post.as_view(), name= 'Creat_Post'),
path('List_Post/', List_Post.as_view(), name= 'List_Post'),
path('Update_post/<pk>', Update_post.as_view(), name='Update_post'),
path('Delet_post/<pk>', Delet_post.as_view(), name='Delet_post'),
path('post_detail/<pk>/', post_detail, name='post_detail'),
path('reply_coment/<pk>/', reply_coment, name='reply_coment'),
path('like/<pk>', like_post, name = 'like_post'),
path('sharePost/<int:post_id>/', sharePost, name='sharePost'),



]
        

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)