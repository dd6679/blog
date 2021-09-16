from django.shortcuts import render, redirect
from .models import Post
from django.core.paginator import Paginator
from .forms import PostForm


def index(request):
    page = request.GET.get('page', '1')
    post_list = Post.objects.filter(user=request.user).order_by('date')
    paginator = Paginator(post_list, 10)
    page_obj = paginator.get_page(page)
    content = {'post_list':page_obj}
    return render(request, 'blog/post_list.html', content)


def detail(request, title):
    post = Post.objects.get(title=title)
    return render(request, 'blog/post_detail.html', {'post':post})


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.post_text = form.cleaned_data['post_text']
            post.public = form.cleaned_data['public']
            post.user = request.user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form':form})