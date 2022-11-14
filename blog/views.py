from django.shortcuts import render
from django.views import
from .models import Post

class PostList(generic.ListView):
    model = Post
