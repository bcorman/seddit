from django.shortcuts import render, redirect
from .models import Profile, Post
from django.contrib.auth.models import User
# Create your views here.

def newest_posts_list(request):
    posts = Post.objects.all().filter(is_comment=False,).order_by('time_stamp')
    return render(request, 'seddit/newest_posts_list.html', {'posts': posts})
