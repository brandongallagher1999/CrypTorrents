from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.TextField()
    length = models.TextField()
    url = models.TextField()
