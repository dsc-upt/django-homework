from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.deletion import CASCADE

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="posts")


