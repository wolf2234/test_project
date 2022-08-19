from django.urls import path, include
from .views import *

urlpatterns = [
    path(r'^basket_adding/', basket_adding, name='basket_adding'),
    path('checkout/', checkout, name='checkout'),
]
