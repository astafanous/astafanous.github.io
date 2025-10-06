
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return self.categoryName

class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_creator")
    imageUrl = models.CharField(max_length=1000)
    excerpt = models.CharField(max_length=1000)
    body = models.CharField(max_length=10000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Post {self.id} made by {self.author} Published on {self.date.strftime('%b %d %Y, %I:%M %p')}"




class Comment(models.Model):
    writor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="userComment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name="listingComment")
    message = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.writor} comment on {self.post}"




class Page(models.Model):
    title = models.CharField(max_length=300)
    imageUrl = models.CharField(max_length=1000)
    content = models.CharField(max_length=6000)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Page {self.id} with title {self.title} Published on {self.date.strftime('%b %d %Y, %I:%M %p')}"




