from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('article/<int:pk>', views.article, name="article"),
    path('article/create', views.CreateArticle.as_view())
]