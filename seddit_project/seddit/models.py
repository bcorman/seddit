from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_url = models.TextField(blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    is_comment = models.BooleanField()
    title = models.CharField(max_length=120, blank=True, null=True)
    body = models.CharField(max_length=1000)
    time_stamp = models.DateTimeField(auto_now_add=True)
    comments = models.ForeignKey('self', on_delete=models.CASCADE)
