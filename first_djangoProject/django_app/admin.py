from django.contrib import admin

#register your models here
from .models import Post
admin.site.register(Post) #to register the post in the administration