from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    category_title = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = 'Article category'
        verbose_name_plural = 'Article categories'

class ArticleModel(models.Model):
    article_title = models.CharField(max_length=50)
    article_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    article_description = models.TextField()
    article_image = models.FileField(upload_to='product_images')
    article_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
