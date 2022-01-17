from django import forms

class PostFormulario(forms.Form):
    title=forms.CharField(max_length=40)
    subtitle=forms.CharField(max_length=40)
    body=forms.CharField(widget=forms.Textarea)

class TagFormulario(forms.Form):
    name=forms.CharField(max_length=40)

class CommentFormulario(forms.Form):
    text=forms.CharField(widget=forms.Textarea)