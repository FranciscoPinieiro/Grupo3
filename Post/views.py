from django.shortcuts import render
from Post import models
from Post import forms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required
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

class CommentDelete(DeleteView):
    model= models.Comment
    success_url = "/Post/postList/"

def commentList(request, post):
    comments=models.Comment.objects.filter(post=post)
    return render(request,"Post/commentList.html",{"comments":comments, "post":post})

def commentForm(request, post):

    if(request.method == "POST"):

        commentForm = forms.CommentForm(request.POST)

        if commentForm.is_valid():

            informacion = commentForm.cleaned_data
            myPost = models.Post.objects.get(id=post)
            comment = models.Comment(text=informacion['text'], post=myPost)
            comment.save()
            comments=models.Comment.objects.filter(post=post)
            return render(request,"Post/commentList.html",{"comments":comments, "post":post})

    else:
        
        commentForm = forms.CommentForm()


    return render(request, "Post/comment_form.html", {"commentForm":commentForm, "post":post})

def login_request(request):

    if request.method =="POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request,"Post/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"Post/Inicio.html", {"mensaje":"error,datos incorrectos"})
        else:
            return render(request, "Post/Inicio.html", {"mensaje":"Error, formulario erroneo"})
    
    form=AuthenticationForm()
    return render(request,"Post/login.html",{'form':form})

def register(request):

    if request.method=='POST':

        #form=UserCreationForm(request.POST)
        form=forms.UserRegisterForm(request.POST)

        if form.is_valid():

            username =form.cleaned_data['username']
            form.save()

            return render (request, "Post/inicio.html" , {"mensaje":"Usuario Creado"})
        
    else:
            form=forms.UserRegisterForm()

        
    return render (request, "Post/registro.html" , {"form":form})

@login_required
def editarPerfil(request):

    usuario=request.user

    if request.method=='POST':

        #form=UserCreationForm(request.POST)
        userEditForm=forms.UserEditForm(request.POST)

        if userEditForm.is_valid():

            informacion = userEditForm.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            return render (request, "Post/inicio.html" , {"mensaje":"Usuario modificado"})
        
    else:
            userEditForm=forms.UserEditForm(initial={'email':usuario.email})

        
    return render(request, "Post/editarPerfil.html" , {"userEditForm":userEditForm, "usuario":usuario})