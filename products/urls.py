from django.urls import path
from . views import *

urlpatterns = [
    path('products', products, name="products"),
    path('product/<int:pk>/<slug:slug>', product_detail, name="product_details"),
]
