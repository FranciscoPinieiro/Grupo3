from django.db import models

class Tag(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=40)
    subtitle=models.CharField(max_length=40)
    body=models.TextField()
    tags=models.ManyToManyField(Tag)
    image=models.ImageField(upload_to='post', null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text=models.TextField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE)