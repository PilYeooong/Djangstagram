from django.urls import path, re_path
from . import views

app_name = 'instagram'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/new/', views.post_new, name='post-new'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/<int:pk>/like/', views.post_like, name='post-like'),
    path('post/<int:pk>/unlike/', views.post_unlike, name='post-unlike'),
    path('post/<int:post_pk>/comment/new/', views.comment_new, name='comment-new'),
    re_path(r'^(?P<username>[\w.@+-]+)/$', views.user_page, name='user-page'),
]