from django import forms
from Post.models import Tag, Post

class PostFormulario(forms.Form):
    title=forms.CharField(max_length=40)
    subtitle=forms.CharField(max_length=40)
    body=forms.CharField(widget=forms.Textarea)
    tags=forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),widget=forms.CheckboxSelectMultiple)

class TagFormulario(forms.Form):
    name=forms.CharField(max_length=40)

class CommentFormulario(forms.Form):
    text=forms.CharField(widget=forms.Textarea)
    post=forms.ModelChoiceField(queryset=Post.objects.all())