from django import forms
from Post import models

class PostForm(forms.Form):
    title=forms.CharField(max_length=40)
    subtitle=forms.CharField(max_length=40)
    body=forms.CharField(widget=forms.Textarea)
    tags=forms.ModelMultipleChoiceField(queryset=models.Tag.objects.all(),widget=forms.CheckboxSelectMultiple)

class TagForm(forms.Form):
    name=forms.CharField(max_length=40)

class CommentForm(forms.Form):
    text=forms.CharField(widget=forms.Textarea)