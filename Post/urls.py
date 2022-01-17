from django.urls import path
from Post import views

urlpatterns = [
    path('',views.posts, name='Post'),
    path('showPost/<id>',views.showPost, name='ShowPost'),
    path('comment/<id>',views.comment, name='Comment'),
    path('postFormulario/', views.postFormulario, name='PostFormulario'),
    path('tagFormulario/', views.tagFormulario, name='TagFormulario'),
    path('commentFormulario/', views.commentFormulario, name='CommentFormulario'),
    path('busquedaPost/', views.busquedaPost, name="BusquedaPost"),
    path('buscar/', views.buscar, name="Buscar"),
]