from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "blog"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('mypage/', views.mypage, name='mypage'),
    path('create/', views.create, name='create'),
    path('modify/<int:post_id>/', views.post_modify, name='post_modify'),
    path('delete/<int:post_id>/', views.post_delete, name='post_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)