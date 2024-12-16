from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def home(request):
    return render(request, 'page/home.html')

def post(request):
    posts = Post.objects.all()
    return render(request, 'page/post.html', {'posts': posts})