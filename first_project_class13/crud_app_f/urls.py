from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard-home', dashboard_home, name='dashboard-home'),
    path('dashboard/banner-add', bannerAdd, name='banner-add'),
    path('dashboard/banner-detail/<pk>', bannerDetail, name='banner-detail'),
    path('dashboard/banner-edit/<title>', bannerEdit, name='banner-edit'),
    path('dashboard/banner-delete/<pk>', bannerDelete, name='banner-delete'),

]