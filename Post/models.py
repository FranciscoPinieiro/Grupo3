from django.db import models

class Tag(models.Model):
    name=models.CharField(max_length=40)

class Post(models.Model):
    title=models.CharField(max_length=40)
    subtitle=models.CharField(max_length=40)
    body=models.TextField()

class Comment(models.Model):
    text=models.TextField()