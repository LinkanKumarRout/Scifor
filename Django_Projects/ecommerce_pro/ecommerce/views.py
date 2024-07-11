import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import *

# view for homepage
def homePage(request):
    products = Products.objects.all()[:18]
    categories = Category.objects.all()
    context = {
        'products':products,
        'categories':categories
    }
    return render(request, 'store/index.html', context=context)

def validate_password(password1, password2):
    if password1 != password2:
        raise ValidationError('Passwords do not match')

    if len(password1) < 8:
        raise ValidationError('Password must be at least 8 characters long')

    if not re.search(r'[A-Z]', password1):
        raise ValidationError('Password must contain at least one uppercase letter')

    if not re.search(r'[a-z]', password1):
        raise ValidationError('Password must contain at least one lowercase letter')

    if not re.search(r'\d', password1):
        raise ValidationError('Password must contain at least one digit')

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password1):
        raise ValidationError('Password must contain at least one special character')

def signup_view(request):
    categories = Category.objects.all()
    context = {
            'categories':categories
    }
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        password = re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', pass1)

        if password is None:
            messages.error(request, 'Your password must be 8 characters and combination of one uppercase, one lowercase, one digit, and one special character atleast.')
            return redirect('signup')  # Redirect back to the signup page
        else:
            if pass1 != pass2:
                messages.error(request, 'Password and Confirm password are not matching')
                return redirect('signup')  # Redirect back to the signup page
            else:
                my_user = User.objects.create_user(uname, email, pass1)
                my_user.is_active = True
                my_user.first_name = first_name
                my_user.last_name = last_name
                my_user.save()
                messages.success(request, 'You have signed up successfully!')
                return redirect('signup')  # Redirect to admin page after successful signup
    return render(request, 'registration/signup.html', context=context)
    

def login_view(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')  # Redirect to home after successful login
        else:
            messages.error(request, 'Invalid credentials!')
    return render(request, 'registration/login.html', context=context)

@login_required
def cart_view(request):
    return render(request, 'store/cart.html')

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart_product, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_product.quantity += quantity
        cart_product.save()
    else:
        cart_product.quantity = quantity
        cart_product.save()
    return redirect('home')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(Cart, pk=item_id)
    item.delete()
    messages.success(request, 'Item removed from cart.')
    return redirect('cart_view')


def category_products(request, category_id):
    # Retrieve the category object based on the category_id
    category = Category.objects.get(pk=category_id)
    all_category = Category.objects.all()
    # Filter products based on the selected category
    products = Products.objects.filter(category=category)

    context = {
        'products': products,
        'selected_category': category,
        'categories':all_category
    }
    return render(request, 'store/category_products.html', context=context)

@login_required
def purchase_view(request):
    if request.method == 'POST':
        user_cart_items = Cart.objects.filter(user=request.user)
        total_amount = sum([item.product.price * item.quantity for item in user_cart_items])
        user_cart_items.delete()
        # Redirect to a purchase confirmation page or the home page
        return render(request, 'store/purchase_confirmation.html', {'total_amount':total_amount})
    return redirect('cart_view')

@login_required
def update_cart(request, item_id):
    if request.method == 'POST':
        try:
            cart_item = Cart.objects.get(id=item_id, user=request.user)
            new_quantity = request.POST.get('quantity')
            if new_quantity and int(new_quantity) > 0:
                cart_item.quantity = int(new_quantity)
                cart_item.save()
        except Cart.DoesNotExist:
            pass
    return redirect('cart_view')

def product_detail(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    return render(request, 'store/product_details.html', {'product': product})
