from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Tag(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=40)
    subtitle=models.CharField(max_length=40)
    body=models.TextField()
    date=models.DateField(default=date.today)
    tags=models.ManyToManyField(Tag)
    image=models.ImageField(upload_to='post', null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text=models.TextField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE)

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares', null=True, blank=True)
    desc=models.TextField()
    link=models.URLField()
    