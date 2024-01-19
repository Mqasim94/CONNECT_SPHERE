from django.db import models
from users.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, default= '11' )
    date_of_birth = models.DateField()
    city = models.CharField(max_length=200)
    bio = models.TextField()
    profile_pic = models.ImageField(default='default.jpg', upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.user.username
    

class Post(models.Model):
    title        = models.CharField(max_length=255)
    content      = models.TextField()
    like         = models.ManyToManyField(User, related_name='likes', blank= True, null= True)
    shared_user  = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    created_on   = models.DateTimeField(default=timezone.now)
    shared_on    = models.DateTimeField(default=timezone.now)
    image        = models.ImageField(upload_to='post_pic', blank=True, null=True)
    is_private   = models.BooleanField(default= False)
   
    
    def __str__(self):
        return  f'{self.title} by {self.shared_user}'
    
    def total_like(self):
        return self.like.count()
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # parent = TreeForeignKey('self', on_delete=models.CASCADE,null=True, blank=True, related_name='children')
    active = models.BooleanField(default=False)
    

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'
    

class ReplyComment(models.Model):
   reply_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
   replier_name = models.ForeignKey(User, on_delete=models.CASCADE)
   reply_content = models.TextField()
   replied_date = models.DateTimeField(default=timezone.now)

   def __str__(self):
       return f'reply by {self.replier_name}on{self.reply_comment}'