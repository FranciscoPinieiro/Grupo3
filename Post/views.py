from django.shortcuts import render
from Post import models
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def inicio(request):
    return render(request, "Post/inicio.html")

class PostList(ListView):
    model= models.Post
    template_name = "Post/postList.html"

class PostDetail(DetailView):
    model= models.Post
    template_name = "Post/postDetail.html"

class PostCreate(CreateView):
    model= models.Post
    success_url = "/Post/postList/"
    fields = ['title', 'subtitle', 'body', 'tags']

class PostUpdate(UpdateView):
    model= models.Post
    success_url = "/Post/postList/"
    fields = ['title', 'subtitle', 'body', 'tags']

class PostDelete(DeleteView):
    model= models.Post
    success_url = "/Post/postList/"

class TagList(ListView):
    model= models.Tag
    template_name = "Post/tagList.html"

class TagCreate(CreateView):
    model= models.Tag
    success_url = "/Post/tagList/"
    fields = ['name']

class TagDelete(DeleteView):
    model= models.Tag
    success_url = "/Post/tagList/"

class CommentList(ListView):
    model= models.Comment
    template_name = "Post/commentList.html"

class CommentCreate(CreateView):
    model= models.Comment
    success_url = "/Post/commentList/"
    fields = ['name','post']

class CommentDelete(DeleteView):
    model= models.Comment
    success_url = "/Post/commentList/"