from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('article/<int:pk>', views.article),
    path('article/create', views.create_article)
]