from django.urls import path, include
from .views import *

urlpatterns = [
    path(r'^product/(?P<product_id>\w+)/', product, name='product')
]
