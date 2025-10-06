from django.contrib import admin
from .models import User, Category, Post, Comment, Page

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Page)
