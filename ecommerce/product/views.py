from django.http import HttpResponse
from django.shortcuts import render

from core.models import Setting
from .models import Category, Product


# Create your views here.


def index(request):
    setting = Setting.objects.filter(status=True).first()
    category = Category.objects.all()
    context = {
        'setting': setting,
        'category': category
    }
    return render(request, 'core/detail.html', context)


def category_products(request, pk, slug):
    setting = Setting.objects.filter(status=True).first()
    category = Category.objects.all()
    products = Product.objects.filter(category_id=pk)
    context = {
        'setting': setting,
        'category': category,
        'products': products,
    }
    return render(request, 'core/shop.html', context)

