from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('product-detail/<pk>', product_detail, name='product-detail'),
]