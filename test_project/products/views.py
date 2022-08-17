from django.shortcuts import render, HttpResponse
from products.models import *


# Create your views here.
def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/product.html', locals())


