from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from core.models import Setting
from order.models import ShopCart
from .forms import CommentForm
from .models import Category, Product, Images, Comment


# Create your views here.


def index(request):
    setting = Setting.objects.filter(status=True).first()
    category = Category.objects.all()
    current_shopcart = ShopCart.objects.filter(user_id=request.user.id)
    total = 0
    for sc in current_shopcart:
        total += sc.product.price * sc.quantity
    context = {
        'setting': setting,
        'category': category,
        "shopcart": current_shopcart
    }
    return render(request, 'core/detail.html', context)


def category_products(request, pk, slug):
    setting = Setting.objects.filter(status=True).first()
    category = Category.objects.all()
    products = Product.objects.filter(category_id=pk)
    current_shopcart = ShopCart.objects.filter(user_id=request.user.id)
    total = 0
    for sc in current_shopcart:
        total += sc.product.price * sc.quantity
    context = {
        'setting': setting,
        'category': category,
        'products': products,
        "shopcart": current_shopcart,
    }
    return render(request, 'core/shop.html', context)


def product_detail(request, pk, slug):
    setting = Setting.objects.filter(status=True).first()
    category = Category.objects.all()
    images = Images.objects.filter(product_id=pk)
    product = get_object_or_404(Product, id=pk)
    comments = Comment.objects.filter(product_id=pk)
    rating = [1, 2, 3, 4, 5]
    current_shopcart = ShopCart.objects.filter(user_id=request.user.id)
    total = 0
    for sc in current_shopcart:
        total += sc.product.price * sc.quantity
    context = {
        'setting': setting,
        'category': category,
        "product": product,
        "images": images,
        "comments": comments,
        "rating": rating,
        "shopcart": current_shopcart,
    }
    return render(request, 'core/detail.html', context)


def add_comments(request, pk):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.rate = form.cleaned_data['rate']
            data.subject = form.cleaned_data['subject']
            data.text = form.cleaned_data['text']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id = pk
            data.user_id = request.user.id
            data.save()
            messages.success(request, 'Your comment is added!')
        else:
            print(form.errors)
    return HttpResponseRedirect(url)
