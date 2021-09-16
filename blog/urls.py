from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('<title>/', views.detail, name='detail'),
]

urlpatterns += static(settings.MEDIA_URL, document)