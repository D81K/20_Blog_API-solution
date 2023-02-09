from django.contrib import admin
from .models import Category, Post, Like, Comment, PostView


# Register your models here.

admin.site.register((Category, Post, Like, Comment, PostView))