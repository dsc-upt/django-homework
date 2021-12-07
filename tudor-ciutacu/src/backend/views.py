from django.http import HttpResponse
from django.shortcuts import render

from .models import Article

# Create your views here.
def all_articles_view(request, *args, **kwargs):
    all_articles = Article.objects.all()
    context = {
        'all_articles_obj': all_articles
    }
    return render(request, 'article/all_articles.html', context)

def article_details_view(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'article/article_details.html', context)

def article_create_view(request):
    if request.method == 'POST':
        my_title = request.POST.get('title')
        my_content = request.POST.get('content')
        f = Article.objects.all()
        ok = True
        for i in f:
            if my_title == i.title:
                ok = False
                break
            print(ok)
        if ok == True:
            Article.objects.create(title=my_title, content=my_content)
    elif request.method == 'GET':
        return render(request, 'article/article_create.html')

    context = {}
    return render(request, 'article/article_create.html', context)
