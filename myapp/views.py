from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def products(request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html')