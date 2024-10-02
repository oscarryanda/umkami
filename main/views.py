from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import datetime
from .models import Product, Category, Cart, CartProduct



@login_required(login_url='/login')
def home_view(request):
    products = Product.objects.filter(user=request.user)
    last_login = request.COOKIES.get('last_login', 'Unknown')  # Use 'Unknown' or any default value you prefer if the cookie doesn't exist
    context = {
        'app': 'UMKaMi',
        'name': request.user.username,
        'class': 'PBP F',
        'products': products,
        'last_login': last_login,
    }

    return render(request, "home.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('main:home_view')
    return render(request, 'confirm_delete.html', {'product': product})


def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('main:home_view')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form, 'product': product})

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user  # Simpan user yang sedang login
        product.save()
        response = HttpResponseRedirect(reverse("main:home_view"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = redirect('main:home_view')
            response.set_cookie('last_login', str(datetime.datetime.now()))  #
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def categories_view(request):
    return render(request, 'categories.html')

def cart_view(request):
    return render(request, 'cart.html')


def products_view(request, category_id=None):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def products_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'products.html', {'products': products, 'category': category})


def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_products = cart.cartproduct_set.all()

    # Calculate total price for each cart product
    for cart_product in cart_products:
        cart_product.total_price = cart_product.product.price * cart_product.quantity

    return render(request, 'cart.html', {'cart': cart, 'cart_products': cart_products})



def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_product.quantity += quantity
        cart_product.save()
    return redirect('main:cart')  # Updated with app namespace


def remove_from_cart(request, product_id):
    cart = Cart.objects.get(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cart_product = CartProduct.objects.get(cart=cart, product=product)
    if request.method == 'POST':
        cart_product.delete()
    return redirect('main:cart')