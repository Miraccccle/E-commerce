from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Setting, ContactForm, ContactMessage
from product.models import Category


# Create your views here.

def index(request):
    setting = Setting.objects.filter(status=True).first()
    category = Category.objects.all()
    context = {
        'setting': setting,
        'category': category
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
