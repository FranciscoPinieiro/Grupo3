from django.urls import path
from Post import views
from django.contrib.auth.views import LogoutView

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
    path('commentList/<post>',views.commentList, name='Comments'),
    path('commentForm/<post>', views.commentForm, name='CommentForm'),
    path('commentDelete/<pk>/', views.CommentDelete.as_view(), name='CommentDelete'),
    path('login/', views.login_request, name='Login'),
    path('register/',views.register, name='Register'),
    path('logout/',LogoutView.as_view(template_name="Post/logout.html"), name='Logout'),
    path('editarPerfil/',views.editarPerfil, name='EditarPerfil'),
]