from django.db import models
from users.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, default= '11' )
    date_of_birth = models.DateField()
    city = models.CharField(max_length=200)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='images/', blank=True, null=True)

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
        return  f'{self.title}'
    
    def total_like(self):
        return self.like.count()