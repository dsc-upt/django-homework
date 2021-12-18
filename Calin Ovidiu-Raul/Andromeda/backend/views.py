from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
# Create your views here.
# " "
def displayArticleObj(request):

    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request,'homework.html',context)

def displayInfo(request,num):
    article = get_object_or_404(Article,pk=num)
    context = {
        'article' : article
    }
    return render(request,'GetData.html',context)

def createArticle(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Article.objects.create(title=title , content=content)
        return redirect('/')
    else:
        return render(request,'Form.html')