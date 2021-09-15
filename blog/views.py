from django.shortcuts import render
from .models import Post


def index(request):
    post_list = Post.objects.order_by('date')
    return render(request, 'blog/post_list.html', {'post_list': post_list})


def detail(request, title):
    post = Post.objects.get(title=title)
    return render(request, 'blog/post_detail.html', {'post':post})