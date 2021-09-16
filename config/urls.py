from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),
]
