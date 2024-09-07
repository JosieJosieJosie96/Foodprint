from django.db import models

class Didyouknow(models.Model):
    comparison_product = models.CharField(max_length=255)
    fact = models.TextField()
    suggestions = models.TextField()

    def __str__(self):
        return self.fact
# Create your models here.
