from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "backend/index.html")

def article(request, pk):
    pass

def create_article(request):
    pass