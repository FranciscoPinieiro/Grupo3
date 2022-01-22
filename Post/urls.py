from django.urls import path
from Post import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('postList/',views.PostList.as_view(), name='Posts'),
    path('postDetail/<pk>/',views.PostDetail.as_view(), name='PostDetail'),
    path('postCreate/', views.PostCreate.as_view(), name='PostCreate'),
    path('postUpdate/<pk>/', views.PostUpdate.as_view(), name='PostUpdate'),
    path('postDelete/<pk>/', views.PostDelete.as_view(), name='PostDelete'),
    path('comment/<id>',views.comment, name='Comment'),
    path('tagFormulario/', views.tagFormulario, name='TagFormulario'),
    path('commentFormulario/', views.commentFormulario, name='CommentFormulario'),
    path('busquedaPost/', views.busquedaPost, name="BusquedaPost"),
    path('buscar/', views.buscar, name="Buscar"),
]