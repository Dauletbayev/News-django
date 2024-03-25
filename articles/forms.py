from django import forms

from articles.models import ArticleModel


class NewsForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = ['article_title', 'article_categories', 'article_tags', 'article_news', 'article_image',
                  'article_author']


class SearchForm(forms.Form):
    search_bar = forms.CharField(max_length=256)
