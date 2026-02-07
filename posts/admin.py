from django.contrib import admin
from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("tag","author","date",)
    list_display = ("title","date","author",)
    prepopulated_fields = {"slug" : ("title",)}    ## For when you don't want to update the save method in models.py

admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)