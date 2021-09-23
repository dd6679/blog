from django.contrib import admin
from .models import Post
from .models import Photo
from .models import Video
from .models import Comment


class VideoInline(admin.TabularInline):
    model = Video


class PhotoInline(admin.TabularInline):
    model = Photo


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    inlines = [PhotoInline, VideoInline,]


admin.site.register(Post, PostAdmin)

