from django.shortcuts import render, redirect

# Create your views here.
from backend.models import Article


def display_all(request):
    a = Article.objects.all()
    context = {
        'afisari': a
    }
    return render(request, "afisare.html", context)

def display_info(request,pk):
    b=Article.objects.get(pk = pk)
    context={
        'info':b
    }
    return render(request, "informatie.html", context)
def display_forms(request):
    if request.method=="POST":
        title=request.POST['title']
        content=request.POST['content']
        Article.objects.create(title=title, content=content)
        return redirect("/")
    elif request.method=="GET":
        return render(request,"form.html")

