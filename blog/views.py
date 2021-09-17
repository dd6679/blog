from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Photo
from django.core.paginator import Paginator
from .forms import PostForm


def index(request):
    page = request.GET.get('page', '1')
    post_list = Post.objects.filter(user=request.user).order_by('date')
    paginator = Paginator(post_list, 10)
    page_obj = paginator.get_page(page)
    content = {'post_list':page_obj}
    return render(request, 'blog/post_list.html', content)


def create(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) #DB save 지연시켜 중복 save 방지
            post.user = request.user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form':form})


def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    content = {'post':post}
    return render(request, 'blog/post_detail.html', content)


def mypage(request):
    return render(request, 'blog/mypage.html')


@login_required(login_url='common:login')
def post_delete(request, title):
    post = get_object_or_404(Post, pk=title)
    if request.user != post.user:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('blog:detail', title=title)
    post.delete()
    return redirect('blog:index')