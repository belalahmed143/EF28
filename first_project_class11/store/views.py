from django.shortcuts import render
from .models import Banner,Product

# Create your views here.
def home(request):
    banner = Banner.objects.all()
    product = Product.objects.all()[1:3]
    cate1_product = Product.objects.filter(category__name='Cate-1')
    last_product = Product.objects.last()
    first_product = Product.objects.first()

    context = {
        'banner':banner,
        'product':product,
        'cate1_product':cate1_product,
        'last_product':last_product,
        'first_product':first_product,
    }
    return render(request, 'store/home.html', context)

def about(request):
    return render(request, 'store/about.html') 