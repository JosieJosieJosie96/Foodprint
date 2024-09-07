from django.db import models

class LandingPage(models.Model):
    scan_qr = models.CharField(max_length=255)
    search_bar = models.CharField(max_length=255)
    filtering_options = models.CharField(max_length=255)

    def __str__(self):
        return f"Landing Page: {self.search_bar}"
