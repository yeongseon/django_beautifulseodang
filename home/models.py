from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=1024)
    body = models.CharField(max_length=4096)
    auth = models.ForeignKey(User)
    date = models.DateTimeField(auto_created=True, auto_now_add=True)