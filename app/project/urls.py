from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from LandingPage.views import scan_dummy_qr


schema_view = get_schema_view(
    openapi.Info(
        title="Foodprint API",
        default_version='v1',
        description="API documentation for Foodprint application",

        contact=openapi.Contact(email="contact@foodprint.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Your other URL patterns...
    path('admin/', admin.site.urls),  # Admin panel route

    # Include your app's API routes
    # path('api/', include('app.urls')),
    # Swagger UI:
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # ReDoc UI:
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Plain JSON and YAML endpoints:
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

path('scan-dummy-qr/', scan_dummy_qr, name='scan_dummy_qr')
]