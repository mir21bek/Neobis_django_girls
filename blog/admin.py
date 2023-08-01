from django.contrib import admin
from .models import Post


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('author', 'title', 'created_date')
    list_filter = ('author', 'published_date')
