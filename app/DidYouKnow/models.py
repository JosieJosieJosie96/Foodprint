from django.db import models


class Didyouknow(models.Model):
    initial_product = models.CharField(max_length=255, default="Product Name")
    comparison_product = models.CharField(max_length=255)
    fact = models.TextField(max_length=255)
    suggestions = models.TextField(max_length=255)

    def __str__(self):
        return f'Fun Fact: {self.fact}'
# Create your models here.
