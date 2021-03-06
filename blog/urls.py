from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('mypage/', views.mypage, name='mypage'),
    path('create/', views.create, name='create'),
    path('modify/<int:post_id>/', views.post_modify, name='post_modify'),
    path('delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('comment_create/<int:post_id>/', views.comment_create, name='comment_create'),
    path('comment_delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]
