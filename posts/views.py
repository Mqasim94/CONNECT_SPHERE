from django.shortcuts import render, render, HttpResponse,  get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from django.views.generic import ListView, DetailView
from .models import Profile, Post, Comment, ReplyComment
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

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class List_Post(ListView):
    model = Post
    template_name = 'posts/List_post.html'


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = post.comments.all()
    new_comment = None

    if request.method == 'POST':
            content = request.POST.get('content')
            post_coment = Comment(content = content , post = post , user = request.user ) 
            post_coment.save()
            return redirect('post_detail', pk=post.id)
    return render(request, 'posts/detail_post.html', {'post': post, 'new_comment': new_comment, 'comments': comments, "id":pk, 'total_likes': post.total_like(), 'is_liked': is_liked })


def reply_coment(request, pk):
    cmnt = get_object_or_404(Comment, id=pk)
    replies = cmnt.replies.all()
    reply = None
    if request.method== "POST":
        reply_content = request.POST.get('reply_content')
        reply_content = ReplyComment(reply_content=reply_content, replier_name=request.user, reply_comment=cmnt)
        reply_content.save()

    return render(request, 'posts/reply_coment.html',{'reply ': reply , 'reply_cmnts':replies})


             
    



