from django.contrib import admin

# Register your models here.

from .models import CategoryModel, ArticleModel

# Register your models here.

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_title', 'created_at']
    search_fields = ['category_title']
    list_filter = ['created_at']

@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['article_title', 'article_created_at']
    search_fields = ['article_title', 'article_category']
    list_filter = ['article_created_at']
