from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,default="")
    last_name = models.CharField(max_length=50,default="")
    bio = models.TextField(max_length=300,default="No bio.",blank=True)
    profile_picture = models.ImageField(upload_to="profile_pictures",default="profile_pictures/nophoto.png")