from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required
# Create your views here.

def articles_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'articles/articles_list.html',{'articles':articles})

def article_detail(request,slug):
    articles = Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'article':articles})

def article_title(request,slug):
    articles = Article.objects.get(slug=slug)
    return render(request, 'articles/base_layout.html',{'article':articles})

@login_required(login_url = '/accounts/login/')
def article_create(request):
    return render(request,'articles/article_create.html')