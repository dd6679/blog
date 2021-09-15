from django.contrib import admin
from .models import Post
from .models import Photo
from .models import Video
from .models import Comment


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']


admin.site.register(Post)
admin.site.register(Photo)
admin.site.register(Video)

