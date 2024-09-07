from rest_framework import viewsets
from models import Didyouknow
from serializers import DidyouknowSerializer

class DidyouknowViewSet(viewsets.ModelViewSet):
    queryset = Didyouknow.objects.all()
    serializer_class = DidyouknowSerializer

