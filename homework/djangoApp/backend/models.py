from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=64)
    phone_number = models.TextField()
    def __str__(self):
        return self.name