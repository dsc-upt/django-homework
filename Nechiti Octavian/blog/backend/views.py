from django.shortcuts import render, get_object_or_404, redirect
from .models import Article


# Create your views here.

def articles_index_view(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }

    return render(request, 'articles/articles_index.html', context)

def article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/article.html', context)

def article_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        content = request.POST.get('content')
        Article.objects.create(title=title, category=category, content=content)
        return redirect('/')
    else:
        return render(request, 'articles/article_create.html')
