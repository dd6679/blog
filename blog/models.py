from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(primary_key=True, max_length=32)
    post_text = models.TextField()
    public = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Video(models.Model):
    post_title = models.ForeignKey('Post', db_column='title', on_delete=models.CASCADE)
    url = models.CharField(max_length=128, null=True, blank=True)


class Photo(models.Model):
    post_title = models.ForeignKey('Post', db_column='title', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/', blank=True, null=True)


class Comment(models.Model):
    post_title = models.ForeignKey('Post', db_column='title', on_delete=models.CASCADE, null=True)
    comment_text = models.TextField(max_length=128)
    public = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)




