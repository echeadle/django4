from audioop import reverse
from multiprocessing import context
from ssl import SSL_ERROR_INVALID_ERROR_CODE
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator

# from .forms import upload_file_exists
import myapp
from . models import Product

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def products(request):
    products = Product.objects.all()
    paginator = Paginator(products,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj
    }
    return render(request, 'myapp/index.html', context)

# Class based view to replace products function 
# class ProductListView(ListView):
#     model = Product
#     template_name = 'myapp/index.html'
#     context_object_name = 'products'
#     paginate_by = 3

# def product_detail(request, id):
#     product = Product.objects.get(id=id)
#     context={
#         'product':product
#     }
#     return render(request, 'myapp/detail.html', context)

# Class based view to replace detailed view.
class ProductDetailView(DetailView):
    model = Product
    template_name = 'myapp/detail.html'
    context_object_name = 'product'

@login_required
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        seller_name = request.user
        product = Product(name=name,price=price,desc=desc,image=image,seller_name=seller_name)
        product.save('/myapp/products')
    return render(request, 'myapp/addproduct.html')

# Class based view for creating a product.
class ProductCreateView(CreateView):
    model = Product
    fields = ['name','price','desc','image','seller_name']
    # product_form.html

def update_product(request, id):
    product = Product.objects.get(id=id)
    image = product.image
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.desc = request.POST.get('desc')
        product.image = request.FILES['upload']
        product.save()
        return redirect('/myapp/products')

    context = {
        'product':product,
    }
    return render(request,'myapp/updateproduct.html',context)

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name','price','desc','image','seller_name']
    template_name_suffix = '_update_form'

def delete_product(request,id):
    product = Product.objects.get(id=id)
    context = {
        'product':product,
    }
    if request.method =='POST':
        product.delete()
        return redirect('/myapp/products')
    return render(request, 'myapp/delete.html',context)

# Create Class based delete view
class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('myapp:products')

def my_listings(request):
    products = Product.objects.filter(seller_name=request.user)
    context = {
        'products':products,
    }
    return render(request,'myapp/mylistings.html',context)