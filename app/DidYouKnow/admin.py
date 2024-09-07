
from django.contrib import admin
from .models import Didyouknow

@admin.register(Didyouknow)
class DidYouKnowAdmin(admin.ModelAdmin):
    list_display = ('comparison_product', 'fact', 'suggestions')


