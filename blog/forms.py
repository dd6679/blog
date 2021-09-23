from django import forms
from .models import Post, Comment
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post_text', 'public']
        widgets = {
            'title':forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username']
        widgets = {
            'username':forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text', 'public']
        widgets = {
            'comment_text':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'style': 'width:1000px; height:150px'
                }
            ),
        }
        labels = {
            'comment_text': '',
            'public': '공개',
        }