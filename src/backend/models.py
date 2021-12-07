from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank = False, null = False)
    date = models.DateField(auto_now_add=True)


