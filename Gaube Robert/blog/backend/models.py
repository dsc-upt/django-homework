from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.deletion import SET_NULL

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True, related_name="posts")

    def __str__(self):
        return self.title


