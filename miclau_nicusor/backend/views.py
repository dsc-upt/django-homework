from django.shortcuts import render, get_object_or_404, redirect

from backend.models import Article


def index_view(request):
    articles = Article.objects.all()
    context = {
        "articles": articles
    }
    return render(request, "index.html", context)

def ar_view(request, pk):
    article = get_object_or_404(Article, pk = pk)
    context = {
        "article": article
    }
    return render(request, "article.html", context)

def create_view(request):
    if request.method == "POST":
        title = request.POST.get("Title")
        content = request.POST.get("Content")
        Article.objects.create(title = title, content = content)
        return redirect("/")
    else:
        return render(request, "article_create.html")