from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=32)
    post_text = RichTextUploadingField()
    public = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    post_id = models.ForeignKey('Post', db_column='post_id', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    comment_text = models.TextField(max_length=128)
    public = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
