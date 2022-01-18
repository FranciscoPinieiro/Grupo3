from django.db import models

class Tag(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=40)
    subtitle=models.CharField(max_length=40)
    body=models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    text=models.TextField()