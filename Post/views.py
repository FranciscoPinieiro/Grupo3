from django.shortcuts import render
from Post import models
from Post import forms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import UserPassesTestMixin

@login_required
def inicio(request):
    user=models.User.objects.get(id=request.user.id)
    avatar=models.Avatar.objects.filter(user=request.user.id)
    if avatar:
        return render(request, "Post/inicio.html", {"imagenURL":avatar[0], "user":user})
    else:
        return render(request, "Post/inicio.html")

def about(request):
    return render(request, "Post/about.html")

@method_decorator(login_required, name='dispatch')
class PostList(ListView):
    model= models.Post
    template_name = "Post/postList.html"

@method_decorator(login_required, name='dispatch')
class PostDetail(DetailView):
    model= models.Post
    template_name = "Post/postDetail.html"

@method_decorator(login_required, name='dispatch')
class PostCreate(CreateView, UserPassesTestMixin):
    model= models.Post
    success_url = "/Post/postList/"
    fields = ['title', 'subtitle', 'body', 'tags', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class PostUpdate(UpdateView):
    model= models.Post
    success_url = "/Post/postList/"
    fields = ['title', 'subtitle', 'body', 'tags', 'image']

@method_decorator(login_required, name='dispatch')
class PostDelete(DeleteView):
    model= models.Post
    success_url = "/Post/postList/"

@method_decorator(login_required, name='dispatch')
class TagList(ListView):
    model= models.Tag
    template_name = "Post/tagList.html"

@method_decorator(login_required, name='dispatch')
class TagCreate(CreateView):
    model= models.Tag
    success_url = "/Post/tagList/"
    fields = ['name']


@method_decorator(login_required, name='dispatch')
class TagDelete(DeleteView):
    model= models.Tag
    success_url = "/Post/tagList/"

@login_required
def postTagList(request,tag):
    blogs = models.Post.objects.filter(tags=tag)
    return render(request,"Post/postList.html",{'object_list':blogs})

@method_decorator(login_required, name='dispatch')
class CommentDelete(DeleteView):
    model= models.Comment
    success_url = "/Post/postList/"

@login_required
def commentList(request, post):
    comments=models.Comment.objects.filter(post=post)
    return render(request,"Post/commentList.html",{"comments":comments, "post":post})

@login_required
def commentForm(request, post):

    if(request.method == "POST"):

        commentForm = forms.CommentForm(request.POST)

        if commentForm.is_valid():

            informacion = commentForm.cleaned_data
            myPost = models.Post.objects.get(id=post)
            user = User.objects.get(username=request.user)
            comment = models.Comment(text=informacion['text'], post=myPost, user=user)
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
                avatar=models.Avatar.objects.filter(user=request.user.id)
                user=models.User.objects.get(id=request.user.id)
                if avatar:
                    return render(request, "Post/inicio.html", {"imagenURL":avatar[0], "user":user})
                else:
                    return render(request, "Post/inicio.html",{"user":user})
            else:
                return render(request,"Post/Inicio.html", {"mensaje":"Error, datos incorrectos"})
        else:
            return render(request, "Post/Inicio.html", {"mensaje":"Error, formulario erroneo"})
    
    form=AuthenticationForm()
    return render(request,"Post/login.html",{'form':form})

def register(request):

    if request.method=='POST':

        #form=UserCreationForm(request.POST)
        form=forms.UserRegisterForm(request.POST)

        if form.is_valid():
            informacion = form.cleaned_data
            form.save()
            user = User.objects.get(username=informacion['username'])
            my_group = Group.objects.get(name='Usuarios') 
            my_group.user_set.add(user)

            return render (request, "Post/inicio.html")
        
    else:
            form=forms.UserRegisterForm()

        
    return render (request, "Post/registro.html" , {"form":form})

@login_required
def verPerfil(request):
    usuario = request.user
    avatar = models.Avatar.objects.filter(user=request.user.id)
    if avatar:
        return render(request, "Post/verPerfil.html", {'usuario':usuario,"avatar":avatar[0]})
    else:
        return render(request, "Post/verPerfil.html", {'usuario':usuario})

@login_required
def editarPerfil(request):

    usuario=request.user

    if request.method=='POST':

        userEditForm=forms.UserEditForm(request.POST, request.FILES)

        if userEditForm.is_valid():

            informacion = userEditForm.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']

            usuario.save()

            user = User.objects.get(username=request.user)
            avatar = models.Avatar.objects.filter(user=user.id)
            if avatar:
                if informacion['imagen']:
                    avatar[0].imagen = informacion['imagen']
                avatar[0].desc = informacion['desc']
                avatar[0].link = informacion['link']
                avatar[0].save()
            else:
                avatar = models.Avatar(user=user, imagen=informacion['imagen'], desc=informacion['desc'], link=informacion['link'])
                avatar.save()
            avatar = models.Avatar.objects.filter(user=user.id)
            return render(request, "Post/verPerfil.html", {'usuario':user,'avatar':avatar[0]})
        
    else:
            avatar=models.Avatar.objects.filter(user=request.user.id)
            if avatar:
                userEditForm=forms.UserEditForm(initial={
                    'email':usuario.email,
                    'first_name':usuario.first_name,
                    'last_name':usuario.last_name,
                    'imagen':avatar[0].imagen,
                    'desc':avatar[0].desc,
                    'link':avatar[0].link
                    })
            else:
                userEditForm=forms.UserEditForm(initial={
                    'email':usuario.email,
                    'first_name':usuario.first_name,
                    'last_name':usuario.last_name
                    })

        
    return render(request, "Post/editarPerfil.html" , {"userEditForm":userEditForm, "usuario":usuario})