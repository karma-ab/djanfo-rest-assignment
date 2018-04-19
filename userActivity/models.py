from django.db import models
from django.utils import timezone


class Post(models.Model):
    user_id = models.CharField(primary_key=True,max_length=200)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200,default="root")


    def __str__(self):
        return self.user_id


class Activity(models.Model):
    userId = models.ForeignKey(Post)
    login = models.DateTimeField(default=timezone.now)
    logout = models.DateTimeField(null=True)
    loginDuration =models.BigIntegerField(null=True)

    def __str__(self):
        return u'%s %s' % (self.login, self.logout)
