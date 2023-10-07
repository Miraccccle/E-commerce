from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Setting, ContactForm, ContactMessage
from product.models import Category, Product
import json


# Create your views here.

def index(request):
    setting = Setting.objects.filter(status=True).first()
    category = Category.objects.all()
    product_slider = Product.objects.order_by('id').all()[:3]
    products = Product.objects.order_by('id').all()
    context = {
        'setting': setting,
        'category': category,
        "product_slider": product_slider,
        "products": products,
    }
    return render(request, 'core/index.html', context)


def contact(request):
    setting = Setting.objects.filter(status=True).first()
    category = Category.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contactMessage = ContactMessage()
            contactMessage.name = form.cleaned_data['name']
            contactMessage.email = form.cleaned_data['email']
            contactMessage.subject = form.cleaned_data['subject']
            contactMessage.message = form.cleaned_data['message']
            contactMessage.ip = request.META.get('REMOTE_ADDR')
            contactMessage.save()
            messages.success(request, 'Message Send')
            return HttpResponseRedirect('/contact/')
    form = ContactForm
    context = {
        'setting': setting,
        'form': form,
        'category': category,
    }
    return render(request, 'core/contact.html', context)


def search(request):
    setting = Setting.objects.filter(status=True).first()
    category = Category.objects.all()
    product_slider = Product.objects.order_by('id').all()[:3]
    if request.method == 'POST':
        query = request.POST['query']
        catId = int(request.POST['cat'])
        print(request.POST, query, catId)
        if catId == 0:
            products = Product.objects.filter(title__icontains=query)
        else:
            products = Product.objects.filter(title__icontains=query, category_id=catId)

    context = {
        'setting': setting,
        'category': category,
        "product_slider": product_slider,
        'products': products,
        'query': query,
    }
    return render(request, 'core/search_results.html', context)


def search_auto(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        q = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=q)
        results = []
        for pl in products:
            results.append(pl.title)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def detail(request):
    setting = Setting.objects.filter(status=True).first()
    category = Category.objects.all()
    context = {
        'setting': setting,
        'category': category
    }
    return render(request, 'core/detail.html', context)


def cart(request):
    setting = Setting.objects.filter(status=True).first()
    category = Category.objects.all()
    context = {
        'setting': setting,
        'category': category
    }
    return render(request, 'core/cart.html', context)


def checkout(request):
    setting = Setting.objects.filter(status=True).first()
    category = Category.objects.all()
    context = {
        'setting': setting,
        'category': category
    }
    return render(request, 'core/checkout.html', context)


def shop(request):
    setting = Setting.objects.filter(status=True).first()
    category = Category.objects.all()
    context = {
        'setting': setting,
        'category': category
    }
    return render(request, 'core/shop.html', context)
