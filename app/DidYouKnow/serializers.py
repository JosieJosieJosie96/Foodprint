from rest_framework import serializers
from models import Didyouknow
class DidyouknowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Didyouknow
        fields = ['comparison_product', 'fact', 'suggestions']