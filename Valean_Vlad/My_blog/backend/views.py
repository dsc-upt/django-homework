from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import ArticleForm


def article_list_view(request):
    queryset = Article.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "display.html", context)


def article_detail_view(request, pk):
    obj = get_object_or_404(Article, id=pk)
    context = {
        "object": obj
    }
    return render(request, "display_each.html", context)


def article_create_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArticleForm()

    context = {
        'form': form
    }
    return render(request, "create_article.html", context)

