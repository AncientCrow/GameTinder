from django.db import models

# Create your models here.


class Card(models.Model):
    icon = models.ImageField
    name = models.CharField(max_length=25)
    games = models.TextField(max_length=1500)
