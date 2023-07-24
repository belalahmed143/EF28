from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    banner = Banner.objects.all().order_by('ordering')[:2]
    banner1 = Banner.objects.all().order_by('ordering')[2:5]
    womens_CLOTHING = Product.objects.filter(category__name='WOMENS CLOTHING')
    mens_CLOTHING = Product.objects.filter(category__name='MENS CLOTHING')
    health_and_beauty = Product.objects.filter(category__name='Health & Beauty')
    bath_and_body = Product.objects.filter(category__name='Bath & Body')
    
  
    context ={
        'banner':banner,
        'banner1':banner1,
        'womens_CLOTHING':womens_CLOTHING,
        'mens_CLOTHING':mens_CLOTHING,
        'health_and_beauty':health_and_beauty,
        'bath_and_body':bath_and_body,
    }
    return render(request, 'store/index.html',context)


def product_detail(request,pk):
    product = Product.objects.get(pk=pk)
    related_product = Product.objects.filter(category=product.category).exclude(pk=pk)

    context = {
        'product':product,
        'related_product':related_product
        }

    return render(request, 'store/product-detail.html',context)


def contact(request):
    return render(request, 'store/contact.html')