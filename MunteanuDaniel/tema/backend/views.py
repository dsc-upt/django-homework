from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

from backend.models import Article

def objects_view(request):
    articles = Article.objects.all()
    context = {}
    context["articles"] = articles
    return render(request, "articles.html", context)

def specific_view(request,nr):
    i = Article.objects.get(pk=nr)
    context = {}
    context["article"] = i
    context["number"] = nr
    return render(request, "specific.html", context)

def form_view(request):
    if request.method == "GET":
        return render(request, "form.html")
    elif request.method == "POST":
        titlu = request.POST["title"]
        continut = request.POST["content"]
        Article.objects.create(title = titlu, content = continut)
        return redirect("/")



