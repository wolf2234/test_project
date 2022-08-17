from django.shortcuts import render, HttpResponse
from .forms import SubscribersForm
from products.models import *
# Create your views here.

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=1)
    products_images_laptops = products_images.filter(product__category__id=2)
    return render(request, 'landing/home.html', locals())


def landing(request):
    name = 'CodingMadved'
    current_day = '09.09.2022'
    form = SubscribersForm(request.POST or None)
    if request.POST and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data.get('name'))
        new_form = form.save()

    return render(request, 'landing/landing.html', locals())


