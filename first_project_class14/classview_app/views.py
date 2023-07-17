from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from store.models import Product

# Create your views here.

# def classview_home(request):
#     return render(request, 'classview_app/home.html')


class ProductListView(ListView):
    model = Product
    # template_name = 'classview_app/home.html'
    # context_object_name = 'products'
    # paginate_by = 2
    
class ProductDetailView(DetailView):
    model = Product
    # template_name = 'classview_app/product-detail.html'

from django.urls import reverse_lazy

class ProductCreateView(CreateView):
    model = Product
    fields = ['name','image','price','category']
    template_name = 'classview_app/product-add.html'
    success_url = reverse_lazy('product-list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name','image','price','category']
    template_name = 'classview_app/product-add.html'
    success_url = reverse_lazy('product-list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'classview_app/product-delete.html'
    success_url = reverse_lazy('product-list')