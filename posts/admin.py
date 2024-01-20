from django.contrib import admin
from .models import Profile, Post, Comment, ReplyComment,Share


admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ReplyComment)
admin.site.register(Share)
