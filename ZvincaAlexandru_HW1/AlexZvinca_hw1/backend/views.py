from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from backend.models import Article


def index_view(request): #add article number
    obj_list = Article.objects.all()
    context = {
        'obj_list': obj_list,
    }
    return render(request, "index_template.html", context)

def content_view(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article': article
    }
    return render(request, "content_template.html", context)

def article_view(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article': article
    }
    return render(request, "article_template.html", context)

def article_create_view(request):
    if(request.method=='GET'):
        return render(request, 'form_template.html')
    elif(request.method=='POST'):
       title = request.POST['title']
       content = request.POST['content']
       Article.objects.create(title=title, content=content)
       return render(request, 'form_template.html')