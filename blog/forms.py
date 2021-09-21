from django import forms
from .models import Post, Photo


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
            'post_text': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'public':forms.NullBooleanSelect(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']