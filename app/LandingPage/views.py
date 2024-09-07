from rest_framework import viewsets
from .models import LandingPage
from .serializers import LandingPageSerializer

class LandingPageViewSet(viewsets.ModelViewSet):
    queryset = LandingPage.objects.all()
    serializer_class = LandingPageSerializer
