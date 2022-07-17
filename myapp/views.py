from django.shortcuts import render
from django.http import HttpResponse
from . models import Product

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def products(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'myapp/index.html', context)

def product_detail(request, id):
    return HttpResponse('The product id is: '+ str(id))