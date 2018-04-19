from django.db import models
from django.utils import timezone


class Post(models.Model):

    name = models.CharField(max_length=200)
    login = models.DateTimeField(default=timezone.now)
    logout = models.CharField(max_length=200)

    def __str__(self):
        return self.name
