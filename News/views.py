import email
from multiprocessing import context
from django.contrib import messages
from unicodedata import name
from django.shortcuts import render
from News.models import *

# Create your views here.


def index(request):
    first_news = News.objects.all()[4]
    side_news = News.objects.all()[5:10]
    three_categories = NewsCategory.objects.all()[2:5]
    context = {'first_news': first_news, 'side_news': side_news,
               'three_categories': three_categories}
    return render(request, 'News/index.html', context)

# def card(request):
#     return render (request,'News/card.html')


def all_news(request):
    all_news = News.objects.all()
    context = {'all_news': all_news}
    return render(request, 'News/all-news.html', context)


def detail(request, id):
    news = News.objects.get(pk=id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['message']
        Comment.objects.create(
            news=news,
            name=name,
            email=email,
            comment=comment
        )
        messages.success(request, 'Comment submitted but is in moderation.')

    category = NewsCategory.objects.get(id=news.category.id)
    rel_news = News.objects.filter(category=category).exclude(id=id)
    comments = Comment.objects.filter(news=news, status=True).order_by('-id')
    context = {'news': news, 'related_news': rel_news, 'comments': comments}
    return render(request, 'News/detail.html', context)

# Fetch all categories:


def all_categories(request):
    Category = NewsCategory.objects.all()
    context = {'Category': Category}
    return render(request, 'News/all-categories.html', context)


def category(request, id):
    category = NewsCategory.objects.get(id=id)
    all_news = News.objects.filter(category=category)
    context = {'category': category, 'all_news': all_news}
    return render(request, 'News/category.html', context)
