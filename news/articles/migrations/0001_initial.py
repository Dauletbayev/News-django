# Generated by Django 5.0.3 on 2024-03-15 19:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Article category',
                'verbose_name_plural': 'Article categories',
            },
        ),
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=50)),
                ('article_description', models.TextField()),
                ('article_image', models.FileField(upload_to='product_images')),
                ('article_created_at', models.DateTimeField(auto_now_add=True)),
                ('article_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.categorymodel')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]