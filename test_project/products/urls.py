from django.urls import path, include
from .views import *

urlpatterns = [
    path('product/(?P<product_id>\w+)', product, name='product')
]
