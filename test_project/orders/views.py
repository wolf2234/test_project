from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.

def basket_adding(request):
    return_dict = dict()
    session_key = request.session.get('session_key', False)
    print(request.POST)
    data = request.POST
    product_id = data.get('product_id')
    nmb = data.get('nmb')
    new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id, defaults={"nmb": nmb})
    if not created:
        new_product.nmn += int(nmb)
        new_product.save(force_update=True)

    product_total_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    product_total_nmb = product_total_basket.count()
    return_dict["product_total_nmb"] = product_total_nmb
    return_dict['products'] = list()


    for item in product_total_basket:
        product_dict = dict()
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        return_dict['products'].append(product_dict)
    return JsonResponse(return_dict)
