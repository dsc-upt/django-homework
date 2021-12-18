from django.shortcuts import render, redirect

# Create your views here.

from backend.models import Article


def index_view(request):
    articles = Article.objects.all()
    context = {'articles' : articles}
    return render(request, "all_articles.html", context)

def create_article(request):
    if request.method == 'GET':
        return render(request, 'create_article.html')
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Article.objects.create(title = title, content = content)

        return redirect('/')

def see_article(request, pk):
    article = Article.objects.get(pk = pk)
    context = {'article' : article}
    return render(request, 'article.html', context)