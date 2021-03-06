from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='generic_profile_picture.png',upload_to='profile_pics')
    bio = models.TextField(null=True, blank=True, default='')

    def __str__(self):
        return f'{self.user.username}'