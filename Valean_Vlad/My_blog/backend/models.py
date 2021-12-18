from django.db import models
from django.urls import reverse


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        # return f"/article/{self.id}/"
        return reverse("article-detail", kwargs={"pk": self.pk})
