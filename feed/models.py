from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class tweet(models.Model):
    uname = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=300, default='')
    pic = models.ImageField(null=True, blank=True, upload_to='images/')
    datetime = models.DateTimeField(default=timezone.now)

