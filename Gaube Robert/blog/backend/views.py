from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Article
from .forms import ArticleForm
from django.views import View

# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, "backend/index.html", {
        "articles" : articles
    })

def article(request, pk):
    article = Article.objects.get(id=pk)
    return render(request, "backend/article.html", {
        "article" : article
    })

class CreateArticle(View):
    def post(self, request):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            text = "Your new article has been saved"
            articles = Article.objects.all()
            return render(request, "backend/index.html", {
                "text": text,
                "articles" : articles
            })
    def get(self, request):
        form = ArticleForm()
        return render(request, "backend/create_article.html", {
            "form" : form,
        })
