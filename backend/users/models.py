from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    username = models.CharField(max_length = 20, unique = True)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True)
    
    USERNAME_FIELD = 'username'

