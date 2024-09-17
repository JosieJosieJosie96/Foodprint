from rest_framework import viewsets
from .models import LandingPage
from .serializers import LandingPageSerializer
from django.shortcuts import render
from django.http import JsonResponse
from pyzbar.pyzbar import decode
from PIL import Image

class LandingPageViewSet(viewsets.ModelViewSet):
    queryset = LandingPage.objects.all()
    serializer_class = LandingPageSerializer


def scan_dummy_qr(request):
    if request.method == 'POST' and request.FILES['qr_image']:
        # Get the uploaded image
        qr_image = request.FILES['qr_image']

        # Open the image using PIL
        img = Image.open(qr_image)

        # Decode the QR code using pyzbar
        decoded_qr = decode(img)

        # Extract the decoded data from the QR code
        if decoded_qr:
            qr_data = decoded_qr[0].data.decode("utf-8")
            return JsonResponse({'data': qr_data})
        else:
            return JsonResponse({'error': 'No QR code found'}, status=400)

    return render(request, 'scan_qr.html')