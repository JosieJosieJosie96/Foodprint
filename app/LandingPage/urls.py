from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LandingPageViewSet

router = DefaultRouter()
router.register(r'landingpages', LandingPageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
