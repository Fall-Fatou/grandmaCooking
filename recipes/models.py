from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    comments = models.TextField()
    ingredients = models.TextField()
    preparation = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
