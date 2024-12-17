from django.contrib import admin
from django.core.paginator import Page
from page.models import Post




@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug','publish']
    list_filter = [ 'publish','created','author']
    search_fields = ['title','body']
    populate_from = ['title','body']