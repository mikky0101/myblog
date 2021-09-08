from app.views import contact
from django.contrib import admin
from .models import Author, Post, Category, Comment, Contact, Reply

# Register your models here.
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Reply)