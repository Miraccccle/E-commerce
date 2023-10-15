from django.shortcuts import render

from core.models import Setting
from order.models import ShopCart
from product.models import Category


# Create your views here.


def index(request):
    setting = Setting.objects.filter(staus=True).first()
    category = Category.objects.all()
    current_shopcart = ShopCart.objects.filter(user_id=request.user.id)
    total = 0
    quantity = 0
    if request.user.is_authenticated:
        current_shopcart = ShopCart.objects.filter(user_id=request.user.id)
        for sc in current_shopcart:
            total += sc.product.price * sc.quantity
            quantity += sc.quantity

    context = {
        'setting': setting,
        'category': category,
        'shopcart': current_shopcart,
        'total': int(total),
        'quantity': quantity,
    }
    return render(request, 'users/user_profile.html', context)


def login_func(request):
    setting = Setting.objects.filter(status=True).first()
    category = Category.objects.all()
    total = 0
    quantity = 0
    current_shopcart = None

    if request.user.is_authenticated:
        current_shopcart = ShopCart.objects.filter(user_id=request.user.id)
        for sc in current_shopcart:
            total += sc.product.price * sc.quantity
            quantity += sc.quantity

    if request.method == 'POST':
        username = request.POST('username')
        password = request.POST('password')
        our

    context = {
        'setting': setting,
        'category': category,
        'shopcart': current_shopcart,
        'total': int(total),
        'quantity': quantity,
    }