
from django.contrib import admin
from .models import Didyouknow

@admin.register(Didyouknow)
class DidYouKnowAdmin(admin.ModelAdmin):
    list_display = ['initial_product', 'comparison_product', 'fact', 'suggestions']
    search_fields = ['initial_product']

