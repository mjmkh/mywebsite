from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_view(request):
    return render(request, 'website/index.html')

def products_view(request):
    return render(request, 'website/products.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    return render(request, 'website/contact.html')

def single_product_view(request):
    return render(request, 'website/single-product.html')