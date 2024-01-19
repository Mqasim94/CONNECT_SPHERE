from django.shortcuts import render, render, HttpResponse,  get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from django.views.generic import ListView, DetailView
from .models import Profile, Post, Comment, ReplyComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# from .forms import Profile_Model_Form


class profile_Create(LoginRequiredMixin, CreateView):
    model = Profile
    fields = '__all__'
    template_name = 'posts/profile.html' 
    success_url = '/posts/List_profile/' 

class Detail_profile(LoginRequiredMixin, DetailView):
    model = Profile
    template_name= 'posts/detail_profile.html'
 
class List_profile(ListView):
    model = Profile
    feilds = '__all__'
    template_name = 'posts/List_profile.html'

class UserPost(ListView):
    model = Post
    template_name = 'posts/Userposts.html'
    feilds = '__all__'

    def get_queryset(self):
        return Post.objects.filter(shared_user=self.request.user)



    

class Update_Profile(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = '__all__'
    template_name = 'posts/update_profile.html'
    success_url = '/posts/List_profile/'

class Delet_profile(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'posts/delet_profile.html'
    success_url = '/posts/List_profile/'





class Creat_Post(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/creat_post.html'
    fields = ['title', 'content', 'created_on', 'image', 'is_private']
    success_url = '/posts/List_Post/'

   

class Update_post(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'created_on', 'image', 'is_private']
    template_name = 'posts/update_post.html'

class Delet_post(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/delet_post.html'
    success_url = '/posts/List_Post/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

@login_required(login_url='/posts/signin/')
def UserProfile(request):

    return render(request, 'posts/userprofile.html')


class List_Post(ListView):
    model = Post
    template_name = 'posts/List_post.html'

    def get_queryset(self):
        return Post.objects.filter(is_private=False)


     

def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = post.comments.all()
    new_comment = None

    if request.method == 'POST':
            content = request.POST.get('content')
            post_coment = Comment(content = content , post = post , user = request.user ) 
            post_coment.save()
            return redirect('posts:post_detail', pk=post.id)

       
    is_liked= True
    if post.like.filter(id=request.user.id). exists(): 
        is_liked = False
        
    return render(request, 'posts/detail_post.html', {'post': post, 'new_comment': new_comment, 'comments': comments, "id":pk, 'total_likes': post.total_like(), 'is_liked': is_liked })


def like_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    is_liked = False
    if post.like.filter(id=request.user.id). exists():
        post.like.remove(request.user)
        is_liked = False
    else:
        post.like.add(request.user)
        is_liked= True
    return redirect('posts:post_detail', pk=post.id)


def reply_coment(request, pk):
    cmnt = get_object_or_404(Comment, id=pk)
    replies = cmnt.replies.all()
    reply = None
    if request.method== "POST":
        reply_content = request.POST.get('reply_content')
        reply_content = ReplyComment(reply_content=reply_content, replier_name=request.user, reply_comment=cmnt)
        reply_content.save()

    return render(request, 'posts/reply_coment.html',{'reply ': reply , 'replies':replies})



