from django.contrib import admin
from .models import Post
from .models import Notice
from .models import News

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'auth', 'body']

class NoticeAdmin(admin.ModelAdmin):
    fields = ['subject', 'name', 'date', 'body']

class NewsAdmin(admin.ModelAdmin):
    fields = ['subject', 'name', 'date', 'body']

admin.site.register(Post, PostAdmin)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(News, NewsAdmin)
