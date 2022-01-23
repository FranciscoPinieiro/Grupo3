from django.urls import path
from Post import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('postList/',views.PostList.as_view(), name='Posts'),
    path('postDetail/<pk>/',views.PostDetail.as_view(), name='PostDetail'),
    path('postCreate/', views.PostCreate.as_view(), name='PostCreate'),
    path('postUpdate/<pk>/', views.PostUpdate.as_view(), name='PostUpdate'),
    path('postDelete/<pk>/', views.PostDelete.as_view(), name='PostDelete'),
    path('tagList/',views.TagList.as_view(), name='Tags'),
    path('tagCreate/', views.TagCreate.as_view(), name='TagCreate'),
    path('tagDelete/<pk>/', views.TagDelete.as_view(), name='TagDelete'),
    path('commentList/',views.CommentList.as_view(), name='Comments'),
    path('commentCreate/', views.CommentCreate.as_view(), name='CommentCreate'),
    path('commentDelete/<pk>/', views.CommentDelete.as_view(), name='CommentDelete'),
]