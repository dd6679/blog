from django import forms
from .models import Post, Photo


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'