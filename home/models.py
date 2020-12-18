from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=15, unique=True)
    lang = models.IntegerField(default=0)
