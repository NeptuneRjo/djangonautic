from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.


def article_list(request):
    articles = Article.objects.all().order_by('date')

    return render(request, 'articles/article_list.html', {'articles': articles})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)

    return render(request, 'articles/article_detail.html', {'article': article})


# reqirects users to /accounts/login if not logged in
@login_required(login_url='accounts:login')
def article_create(request):
    if request.method == 'POST':
        # files are not included in the POST data
        form = forms.CreateArticle(request.POST, request.FILES)

        if form.is_valid():
            # save article to db
            return redirect('articles:list')

    else:
        form = forms.CreateArticle()

    return render(request, 'articles/article_create.html', {'form': form})
