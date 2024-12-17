from django.shortcuts import render
from .models import Post


def home(request):
    return render(request, 'page/home.html')

def post(request):
    posts = Post.published.all()
    return render(request, 'page/post.html', {'posts': posts})
