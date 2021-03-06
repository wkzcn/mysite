from django.contrib import admin

from .models import ArticleCategory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'article_statistics', 'created_time')
    ordering = ('created_time', )
    list_per_page = 20


admin.site.register(ArticleCategory, CategoryAdmin)
