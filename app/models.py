from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User 
from django.shortcuts import reverse

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    about = models.TextField(default="input your about info")
    top = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={
            'pk': self.id
        })     

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    has_comment = models.BooleanField(default=False)
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username  

    @property
    def reply(self):
        return self.reply_set.all()         

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"{self.user} on {self.comment.post}"     


class Post(models.Model):
    content = HTMLField()
    content2 = RichTextField(null=True, blank=True)
    title = models.CharField(max_length=50)
    overview = models.CharField(max_length=400)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    main_cat = models.CharField(default="Technology", max_length=20)
    Category = models.ManyToManyField(Category)
    thumbnail = models.ImageField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={
            'pk': self.id
        })        

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')    

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()    


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.name