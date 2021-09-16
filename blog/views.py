from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator


def index(request):
    page = request.GET.get('page', '1')
    post_list = Post.objects.order_by('date')
    paginator = Paginator(post_list, 10)
    page_obj = paginator.get_page(page)
    content = {'post_list':page_obj}
    return render(request, 'blog/post_list.html', content)


def detail(request, title):
    post = Post.objects.get(title=title)
    return render(request, 'blog/post_detail.html', {'post':post})