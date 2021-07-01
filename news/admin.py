from django.contrib import admin
from .models import Author, Article


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
