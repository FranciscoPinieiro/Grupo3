from django.shortcuts import render

from Post.models import Post, Tag, Comment

def posts(request):
    posts=Post.objects.all()
    return render(request,'index.html',{"posts":posts})

def showPost(request,id):
    post=Post.objects.get(id=id)
    tags=Tag.objects.filter(post__id=id)
    return render(request, 'show.html', {"post":post, "tags":tags})

def comment(request,id):
    comment=Comment.objects.get(id=id)
    return render(request, 'comment.html', {"comment":comment})