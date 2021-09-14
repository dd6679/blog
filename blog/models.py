from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    password = models.CharField(max_length=32)
    nickname = models.CharField(max_length=10)
    email = models.CharField(max_length=128)


class Posts(models.Model):
    title = models.CharField(primary_key=True, max_length=32)
    post_text = models.TextField()
    public = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    #image = models.ImageField()
    #video = models.CharField(max_length=128, blank=True, null=True) n개..


class Comment(models.Model):
    post_title = models.ForeignKey('Posts', db_column='title', on_delete=models.CASCADE, null=True)
    comment_text = models.TextField(max_length=128)
    public = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)




