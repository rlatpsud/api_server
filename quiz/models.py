from django.db import models

# Create your models here.
class Multiple(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()

class OX(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()

class Test(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()