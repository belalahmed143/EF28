from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('product-search', product_search, name='product-search'),
    path('product-detail/<pk>', product_detail, name='product-detail'),
    path('category-filtering/<pk>', category_filtering, name='category-filtering'),
]