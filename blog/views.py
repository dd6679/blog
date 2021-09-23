from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Photo, Comment
from django.core.paginator import Paginator
from .forms import PostForm, CustomUserChangeForm, CommentForm
from django.utils import timezone


def index(request):
    page = request.GET.get('page', '1')
    post_list = Post.objects.filter(user=request.user).order_by('-date')
    paginator = Paginator(post_list, 7)
    page_obj = paginator.get_page(page)
    content = {'post_list': page_obj}
    return render(request, 'blog/post_list.html', content)


def create(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # DB save 지연시켜 중복 save 방지
            post.user = request.user
            post.save()
            for img in request.FILES.getlist('imgs'):
                photo = Photo()
                photo.post_id = post
                photo.image = img
                photo.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})


def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    photo = Photo.objects.filter(post_id=post_id)
    comment_form = CommentForm()
    content = {'post': post, 'photo': photo, 'comment_form': comment_form}
    return render(request, 'blog/post_detail.html', content)


@login_required(login_url='common:login')
def mypage(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'blog/mypage.html', {'form': form})


@login_required(login_url='common:login')
def post_modify(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.user:
        messages.error(request, '수정권한이 없습니다')
        return redirect('blog:detail', post_id=post.id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = timezone.now()  # 수정일시 저장
            post.save()
            for img in request.FILES.getlist('imgs'):
                photo = Photo()
                photo.post_id = post
                photo.image = img
                photo.save()
            return redirect('blog:detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    context = {'form': form}
    return render(request, 'blog/post_create.html', context)


@login_required(login_url='common:login')
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.user:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('blog:detail', post_id=post.id)
    post.delete()
    return redirect('blog:index')


@login_required(login_url='common:login')
def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.date = timezone.now()
            comment.post_id = post
            comment.save()
            return redirect('blog:detail', post_id=post_id)
    else:
        form = CommentForm()
    return redirect(request, 'blog:detail', {'form': form})


# @login_required(login_url='common:login')
# def comment_modify(request, comment_id):
#     comment = get_object_or_404(Comment, pk=comment_id)
#     if request.user != comment.author:
#         messages.error(request, '댓글 수정 권한이 없습니다')
#         return redirect('blog:detail', post_id=comment.post_id.id)
#     if request.method == "POST":
#         form = CommentForm(request.POST, instance=comment)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.date = timezone.now()
#             comment.save()
#             return redirect('blog:detail', post_id=comment.post_id.id)
#     else:
#         form = CommentForm(instance=comment)
#     return redirect(request, 'blog:detail', {'form':form})


@login_required(login_url='common:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글 삭제 권한이 없습니다')
        return redirect('blog:detail', post_id=comment.post_id.id)
    else:
        comment.delete()
    return redirect('blog:detail', post_id=comment.post_id.id)
