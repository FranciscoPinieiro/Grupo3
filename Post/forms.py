from django import forms
from Post import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentForm(forms.Form):
    text=forms.CharField(widget=forms.Textarea)

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir la Contraseña',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields= ['username','email','password1','password2']
        help_texts = {k:""for k in fields}

class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Modificar E-mail")
    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir la Contraseña',widget=forms.PasswordInput)
    first_name=forms.CharField(label='Nombre')
    last_name=forms.CharField(label='Apellido')
    

    class Meta:
        model = User
        fields= ['email','password1','password2','first_name','last_name']
        help_texts = {k:""for k in fields}

class AvatarForm(forms.Form):
    imagen=forms.ImageField()
    desc=forms.CharField(widget=forms.Textarea, label='Descripcion')
    link=forms.URLField(label='Pagina web personal')