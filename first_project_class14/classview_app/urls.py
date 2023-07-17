from django.urls import path
from .views import *

urlpatterns = [
    path('class-base-view', ProductListView.as_view(template_name = 'classview_app/home.html'),name='product-list'),
    path('product-detail/<pk>', ProductDetailView.as_view( template_name = 'classview_app/product-detail.html'), name='product-detail'),
    path('product-add/', ProductCreateView.as_view(), name='product-add'),
    path('product-edit/<pk>', ProductUpdateView.as_view(), name='product-edit'),
    path('product-delete/<pk>', ProductDeleteView.as_view(), name='product-delete'),
]