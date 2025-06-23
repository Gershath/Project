# app/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('auth/', views.auth_view, name='auth'),  # This links to the auth page
    path("home/", views.home, name='home'),
    path("about/", views.about, name='about'),
    path('product/', views.product_list, name='product_list'),
    path('contact/', views.contact, name='contact'),



    path('login/', views.login_view, name='login'),  # If you want custom login view, else use default LoginView
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'), 
    path('signup/', views.signup, name='signup'),

    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout-success/', views.checkout_success, name='checkout_success'),


]
