from django.db import models, transaction

from ramailo.models.base import BaseModel
from ramailo.models.blog.category import Category
from ramailo.models.user import User


class Post(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=200, default="")
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='posts')
    
    def __str__(self):
        return f"Post(Title: {self.title}, Content: {self.content}, Category: {self.content}, Is Published: {self.is_published}, Author: {self.author})"