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
        return self.city
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    shared_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    shared_on = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post_pic', blank=True, null=True)
    
    
    def __str__(self):
        return  f'{self.shared_user.username} post {self.title}'