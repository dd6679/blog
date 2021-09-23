from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request, username=None):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
        if User.objects.filter(username=username).first():
            messages.error(request, "This username is already taken")
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
