from django.shortcuts import render,redirect
from store.models import *
from .forms import *
# Create your views here.

def dashboard_home(request):
    banner = Banner.objects.all()

    context ={
        'banner':banner
    }
    return render(request, 'crud_app_f/dashboard-home.html',context)

def bannerAdd(request):
    form = BannerForm()
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard-home')
    context ={
        'form':form
    }
    return render(request, 'crud_app_f/banner-add.html',context)


def bannerDetail(request,pk):
    banner = Banner.objects.get(pk=pk)
    context ={
        'banner':banner
    }
    return render(request, 'crud_app_f/banner-detail.html',context)


def bannerEdit(request,title):
    banner = Banner.objects.get(title=title)
    form = BannerForm(instance=banner)

    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            form.save()
            return redirect('dashboard-home')
    context ={
        'form':form
    }
    return render(request, 'crud_app_f/banner-add.html',context)


def bannerDelete(request,pk):
    banner = Banner.objects.get(pk=pk)
    banner.delete()
    return redirect('dashboard-home')