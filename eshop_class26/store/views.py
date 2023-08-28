from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

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

from django.db.models import Q

# name
# category
# price
# discount_price
# description



def product_search(request):
    query = request.GET['q']

    lookups = Q(name__icontains=query) | Q(price__icontains=query) | Q(discount_price__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query)
    search_result = Product.objects.filter(lookups)
    return render(request, 'store/search.html', {'search_result':search_result})


from django.core.paginator import Paginator

def category_filtering(request,pk):
    cat = Category.objects.get(pk=pk)
    products = Product.objects.filter(Q(category=cat.id) | Q(category__main_category=cat.id))

    paginator = Paginator(products, 1)
    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(request, 'store/category-filter.html',{'page_obj':page_obj})

def contact(request):
    return render(request, 'store/contact.html')



def registration(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={
        'form':form
    }
    return render(request, 'store/registration.html',context)


@login_required
def profile(request):
    return render(request, 'store/profile.html')


@login_required
def profile_update(request):
    user_form = UserUpdateForm(instance=request.user)
    profile_form = UserProfileUpdateForm(instance=request.user.profile)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = UserProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    context ={
        'profile_form':profile_form,
        'user_form':user_form
    }
    return render(request, 'store/profile-update.html', context)
    


from django.contrib import messages
from django.shortcuts import get_object_or_404

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_product, created = CartProduct.objects.get_or_create(product=product, user=request.user, ordered=False)
    order_qs = OrderedProduct.objects.filter(user=request.user,ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        if order.cart_product.filter(product__pk=product.pk).exists():
            cart_product.quantity += 1
            cart_product.save()
            messages.info(request, 'This product quantity updated')
            return redirect('product-detail',pk=pk)
        else:
            order.cart_product.add(cart_product)
            messages.success(request, 'This product was add to cart')
            return redirect('product-detail',pk=pk)
    else:
        order = OrderedProduct.objects.create(user=request.user)
        order.cart_product.add(cart_product)
        messages.success(request, 'This product was add to cart')
        return redirect('product-detail',pk=pk)
    return redirect('product-detail',pk=pk)

def remove_from_cart(request,pk):
    product = get_object_or_404(Product, pk=pk)
    order_qs = OrderedProduct.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.cart_product.filter(product__pk=product.pk).exists():
            cartproduct = CartProduct.objects.filter(user=request.user,ordered=False,product__pk=product.pk)[0]
            cartproduct.delete()
            messages.success(request,'This product remove from cart')
            return redirect('product-detail', pk=pk)
        else:
            messages.info(request, 'This product was not your cart')
            return redirect('product-detail', pk=pk)
    else:
        messages.info(request,'This product was not your cart')
        return redirect('product-detail', pk=pk)
    return redirect('product-detail', pk=pk)