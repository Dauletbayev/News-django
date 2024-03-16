from django.shortcuts import render

from articles.models import CategoryModel, ArticleModel


# Create your views here.

def tech_index(request):
    categories = CategoryModel.objects.all()
    articles = ArticleModel.objects.all()
    context = {'categories': categories, 'articles': articles}
    return render(request, template_name='tech_index.html', context=context)

def tech_category_01(request):
    categories = CategoryModel.objects.all()
    articles = ArticleModel.objects.all()
    context = {'categories': categories, 'articles': articles}
    return render(request, template_name='tech_category_01.html', context=context)

def tech_category_02(request):
    categories = CategoryModel.objects.all()
    articles = ArticleModel.objects.all()
    context = {'categories': categories, 'articles': articles}
    return render(request, template_name='tech_category_02.html', context=context)

def tech_category_03(request):
    categories = CategoryModel.objects.all()
    articles = ArticleModel.objects.all()
    context = {'categories': categories, 'articles': articles}
    return render(request, template_name='tech_category_03.html', context=context)

def tech_single(request):
    categories = CategoryModel.objects.all()
    articles = ArticleModel.objects.all()
    context = {'categories': categories, 'articles': articles}
    return render(request, template_name='tech_author.html', context=context)

def tech_contact(request):
    categories = CategoryModel.objects.all()
    articles = ArticleModel.objects.all()
    context = {'categories': categories, 'articles': articles}
    return render(request, template_name='tech_contact.html', context=context)

def tech_author(request):
    categories = CategoryModel.objects.all()
    articles = ArticleModel.objects.all()
    context = {'categories': categories, 'articles': articles}
    return render(request, template_name='tech_author.html', context=context)