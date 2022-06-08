from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=10)
    rate = models.IntegerField(max_length=10, default=0)
    free = models.BooleanField(max_length=10, default=True)