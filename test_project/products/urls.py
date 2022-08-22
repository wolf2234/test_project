from django.urls import path, include
from .views import *

urlpatterns = [
    path('product/<product_id>/', product, name='product')
]
