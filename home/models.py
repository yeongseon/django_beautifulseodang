from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=1024)
    body = RichTextField(max_length=4096)
    auth = models.ForeignKey(User)
    date = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.title

class Post_media(models.Model):
    title = models.CharField(max_length=1024)
    body = models.CharField

class Notice(models.Model):
    subject = models.CharField(max_length=1024, blank=True)
    name = models.CharField(max_length=32, blank=True)
    date = models.DateField(null=True, blank=True)
    body = RichTextField(max_length=4096)
    hits = models.IntegerField(default=0, blank=True)

class News(models.Model):
    subject = models.CharField(max_length=1024, blank=True)
    name = models.CharField(max_length=32, blank=True)
    date = models.DateField(null=True, blank=True)
    body = RichTextField(max_length=4096)
    hits = models.IntegerField(default=0, blank=True)

class People(models.Model):
    type = models.CharField(max_length=32, blank=True)
    name = models.CharField(max_length=32, blank=True)
    carrier = models.CharField(max_length=1024, blank=True)
    region = models.CharField(max_length=32, blank=True)
    image = models.CharField(max_length=1024, blank=True)


class Content(models.Model):
    type = models.CharField(max_length=32, default="")
    number = models.IntegerField()
    name = models.CharField(primary_key=True, max_length=32, default="")
    author = models.CharField(max_length=32, default="")
    img = models.CharField(max_length=1024, default="")

class Donation(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    amount = models.IntegerField()
    def __str__(self):
        return self.id

class Book(models.Model):
    sort = models.CharField(max_length=32, default="")
    id = models.IntegerField()
    name = models.CharField(primary_key=True, max_length=32, default="")
    author = models.CharField(max_length=32, default="")
    img = models.CharField(max_length=1024, default="")
    def __str__(self):
        return self.name