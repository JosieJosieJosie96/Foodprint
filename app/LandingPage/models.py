from django.db import models

class LandingPage(models.Model):
    search_bar = models.CharField(max_length=255)



class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def __str__(self):
        return f"Landing Page: {self.search_bar}"
