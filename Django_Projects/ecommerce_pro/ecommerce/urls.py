from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('home', views.homePage, name='home'),
    path('signup',views.signup_view, name='signup'),
    path('login',views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cart-details',views.cart_view, name='cart_view'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('category-products/<int:category_id>',views.category_products, name='category_products'),
    path('purchase/', views.purchase_view, name='purchase_view'),
    path('update_cart/<int:item_id>/', views.update_cart, name='update_cart'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('accounts/profile/', views.login_view),
]
