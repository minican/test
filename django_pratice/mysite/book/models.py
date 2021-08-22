from django.db import models

# Create your models here.
class book(models.Model):
    bid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    press = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    translator = models.CharField(max_length=255)
    publication_year = models.DateField()
    page_num = models.IntegerField()
    price = models.FloatField()
    type = models.CharField(max_length=255)