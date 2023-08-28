from django.urls import path
from .views import *

from store import views as user_views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('product-search', product_search, name='product-search'),
    path('product-detail/<pk>', product_detail, name='product-detail'),
    path('category-filtering/<pk>', category_filtering, name='category-filtering'),
    path('add-to-cart/<pk>', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<pk>', remove_from_cart, name='remove-from-cart'),
    path('quantity-increment/<pk>',cart_product_quantity_increment,name='quantity-increment'),
    path('quantity-decrement/<pk>',cart_product_quantity_decrement,name='quantity-decrement'),







    path('register',user_views.registration, name='register'),
    path('profile',user_views.profile, name='profile'),
    path('profile-update',user_views.profile_update, name='profile-update'),


    path('login/', auth_views.LoginView.as_view(template_name='store/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='store/logout.html'), name='logout'),


    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='store/password_change.html'), name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='store/password_change_done.html'), name='password_change_done'),
    
    
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='store/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='store/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='store/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='store/password_reset_complete.html'),name='password_reset_complete'),


]