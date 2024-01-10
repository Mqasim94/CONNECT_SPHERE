from django.db import models
from users.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, default= '11' )
    date_of_birth = models.DateField()
    city = models.CharField(max_length=200)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.city
    