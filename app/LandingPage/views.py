from rest_framework import viewsets
from .models import LandingPage
from .serializers import LandingPageSerializer
from django.shortcuts import render
from django.http import JsonResponse
from pyzbar.pyzbar import decode
from PIL import Image
from .models import LandingPage
from .models import Product
from .forms import ProductFilterForm

class LandingPageViewSet(viewsets.ModelViewSet):
    queryset = LandingPage.objects.all()
    serializer_class = LandingPageSerializer

def search_view(request):
    query = request.GET.get('q')  # Get the 'q' parameter from the URL
    results = LandingPage.objects.filter(name__icontains=query) if query else []
    return render(request, 'search_results.html', {'results': results, 'query': query})


def product_list(request):
    products = Product.objects.all()  # Start with all products
    form = ProductFilterForm(request.GET)  # Bind the form to the GET data

    if form.is_valid():
        name = form.cleaned_data.get('name')
        category = form.cleaned_data.get('category')
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        # Apply filters based on form input
        if name:
            products = products.filter(name__icontains=name)
        if category:
            products = products.filter(category__icontains=category)
        if min_price:
            products = products.filter(price__gte=min_price)
        if max_price:
            products = products.filter(price__lte=max_price)

    return render(request, 'product_list.html', {'products': products, 'form': form})


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