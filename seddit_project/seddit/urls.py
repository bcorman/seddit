from django.urls import path
from . import views

urlpatterns = [
    path('', views.newest_posts_list, name='newest_posts_list'),
]
