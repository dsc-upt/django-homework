from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from Aplicatie_1.models import Article


def hello_view(request):
    return HttpResponse("Hello!")


def items_view(request):
    return HttpResponse("This is the items page")


def item_view(request, Number):
    Article.objects.get(pk=Number)
    context={
        'article': Article

    }
    return render(request, "article_template.html", context)

def article_view(request):
    articles=Article.objects.all()
    context={}
    context['articles']=articles
    return render(request, 'all_articles_template.html', context)

def createArticle_view(request):
    if request.method == "POST":
        name = request.POST["title"]
        phone = request.POST["content"]
        Article.objects.create(title=name, content=phone)

        articles = Article.objects.all()
        context = {}
        context['articles'] = articles
        return render(request, 'all_articles_template.html', context)

    elif request.method == "GET":
        return render(request, 'form_template.html')



