from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(default = 'Write content here')
    date = models.DateField(auto_now_add=True)