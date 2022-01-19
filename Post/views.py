from django.shortcuts import render
from django.http import HttpResponse
from Post.models import Post, Tag, Comment
from Post.forms import PostFormulario, TagFormulario, CommentFormulario

def posts(request):
    posts=Post.objects.all()
    return render(request,'index.html',{"posts":posts})

def inicio(request):
    return render(request, "inicio.html")

def comment(request,id):
    comment=Comment.objects.get(id=id)
    return render(request, 'comment.html', {"comment":comment})

def postFormulario(request):

    if(request.method == "POST"):

        miFormulario = PostFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            post = Post(title=informacion['title'], subtitle=informacion['subtitle'], body=informacion['body'])
            post.save()
            posts=Post.objects.all()
            return render(request,'index.html',{"posts":posts})

    else:
        
        miFormulario = PostFormulario()


    return render(request, "postFormulario.html", {"miFormulario":miFormulario})

def tagFormulario(request):

    if(request.method == "POST"):

        miFormulario = TagFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            tag = Tag(name=informacion['name'])
            tag.save()
            return render(request,'inicio.html')

    else:
        
        miFormulario = TagFormulario()


    return render(request, "tagFormulario.html", {"miFormulario":miFormulario})

def commentFormulario(request):

    if(request.method == "POST"):

        miFormulario = CommentFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            post = Comment(text=informacion['text'])
            post.save()
            return render(request,'inicio.html')

    else:
        
        miFormulario = CommentFormulario()


    return render(request, "commentFormulario.html", {"miFormulario":miFormulario})

def busquedaPost(request):
    return render(request, "busquedaPost.html")

def buscar(request):

    if request.GET["title"]:

        title=request.GET["title"]
        posts = Post.objects.filter(title=title)

        return render(request, "resultadosBusqueda.html", {"posts":posts, "title":title})

    else:

        respuesta= "No enviaste datos"

    return HttpResponse(respuesta)