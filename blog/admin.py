from blog.models import *
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    display_fields = ["title", "created"]

class CommentAdmin(admin.ModelAdmin):
    display_fields = ["post", "author", "created"]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
