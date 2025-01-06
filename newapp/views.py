from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from newapp.models import *

def product(request):
    products = Product.objects.all() 
    return render(request,"newapp/product.html", {'products': products})


def show_products(request,prod_id):
    cats = get_object_or_404(Product, pk=prod_id)
    
    context = {
        'cats': cats,
        'name': cats.name,
        'category': cats.category,
        'cat_selected': cats.category_id,
    }

    return render(request,"newapp/about_products.html", context=context)

