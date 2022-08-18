from django.shortcuts import render, HttpResponse
from products.models import *
import random
import string

# Create your views here.

def product(request, product_id):
    product = Product.objects.get(id=product_id)

    session_key = request.session.get('session_key', False)
    if not session_key:
        request.session['session_key'] = ''.join(random.choices((string.ascii_lowercase + string.ascii_uppercase+string.ascii_letters), k=8))
        request.session.modified = True
    print(request.session.get('session_key'))

    return render(request, 'products/product.html', locals())


