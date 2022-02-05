from django.contrib import admin

from Post.models import Post, Tag, Comment, Avatar

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Avatar)