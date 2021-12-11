from django.shortcuts import render, redirect

# Create your views here.
from backend.models import Article


def article_list_view(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, "articles.html", context)


def article_view(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, "article.html", context)


def myform_view(request):
    if request.method == "GET":
        return render(request, "myform_template.html")
    elif request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        Article.objects.create(title=title, content=content)
        return redirect("/")

