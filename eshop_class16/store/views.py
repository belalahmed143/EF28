from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    banner = Banner.objects.all().order_by('ordering')[:2]
    banner1 = Banner.objects.all().order_by('ordering')[2:5]
    womens_CLOTHING = Product.objects.filter(category__name='WOMENS CLOTHING')
    mens_CLOTHING = Product.objects.filter(category__name='MENS CLOTHING')
    context ={
        'banner':banner,
        'banner1':banner1,
        'womens_CLOTHING':womens_CLOTHING,
        'mens_CLOTHING':mens_CLOTHING,
    }
    return render(request, 'store/index.html',context)

def contact(request):
    return render(request, 'store/contact.html')