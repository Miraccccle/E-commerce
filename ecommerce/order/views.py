from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.utils.crypto import get_random_string

from core.models import Setting
from product.models import Category, Product
from users.models import UserProfile
from .models import ShopCart, Order, OrderProduct
from .forms import ShopCartForm, OrderForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return HttpResponse('Страница Order')


@login_required(login_url='/login')
def addtoshopcart(request, pk):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checkproduct = ShopCart.objects.filter(product_id=pk, user_id=request.user.id)

    if checkproduct:
        control = 1  # товар в корзине
    else:
        control = 0  # товар не в корзине

    if request.method == "POST":
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:  # Обновляем корзину
                data = ShopCart.objects.get(product_id=pk, user_id=request.user.id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
                messages.success(request, 'Корзина обновлена')
            else:  # добавляем в корзину
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = pk
                data.quantity = form.cleaned_data['quantity']
                data.save()
                messages.success(request, 'Товар добавлен в корзину')
        return HttpResponseRedirect(url)
    else:  # если это не РОST запрос
        if control == 1:
            data = ShopCart.objects.get(product_id=pk, user_id=request.user.id)
            data.quantity += 1  # если еще раз ткнули добавить тот же товар
            data.save()
            messages.success(request, 'Корзина обновлена')
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = pk
            data.quantity = 1  # только 1 товар
            data.save()
            messages.success(request, 'Товар добавлен в корзину')
        return HttpResponseRedirect(url)


def shopcart(request):
    setting = Setting.objects.filter(status=True).first()
    category = Category.objects.all()
    current_shopcart = ShopCart.objects.filter(user_id=request.user.id)
    total = 0
    for sc in current_shopcart:
        total += sc.product.price * sc.quantity

    context = {
        'setting': setting,
        'category': category,
        'shopcart': current_shopcart,
        'total': total
    }
    return render(request, 'core/cart.html', context)


def checkout(request):
    current_user = request.user
    setting = Setting.objects.filter(status=True).first()
    category = Category.objects.all()
    shopcart = ShopCart.objects.filter(user_id=request.user.id)
    total = 0
    quantity = 0
    for sc in shopcart:
        total += sc.product.price * sc.quantity
        quantity += sc.quantity

    profile = UserProfile.objects.get(user_id=current_user.id)

    if request.method == 'POST':
        print('ПОСТ ЗАПРОС')
        form = OrderForm(request.POST)
        if form.is_valid():
            # Не забудьте проверить информацию о кредитной карте пользователя и возможности оплаты
            # на реальном проекте
            # Получаем информацию из формы пользователя
            data = Order()
            data.first_name = form.cleaned_data['first_name']  # get product quantity from form
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            # случайная строка из 5 символов - код заказа
            ordercode = get_random_string(5).upper()
            data.code = ordercode
            data.save()

            # Далее - получаем информацию из корзины и перебираем товары
            # добавляем их в заказ, уменьшаем остатки на складе
            shopcart = ShopCart.objects.filter(user_id=current_user.id)
            for s in shopcart:
                detail = OrderProduct()
                detail.order_id = data.id  # ID заказа (сформировали случайно)
                detail.product_id = s.product_id  # ID Товара
                detail.user_id = current_user.id  # ID пользователя
                detail.quantity = s.quantity  # количество
                detail.price = s.product.price  # цена
                detail.amount = s.amount  # итоговая сумма по этому товару
                detail.save()
                product = Product.objects.get(id=s.product_id)
                product.amount -= s.quantity  # Уменьшаем количество товара
                product.save()  # сохраняем заказ в БД

            # очищаем корзину после формирования заказа - удаляем из БД
            ShopCart.objects.filter(user_id=current_user.id).delete()
            request.session['cart_items'] = 0  # количество товаров в корзине - обнуляем
            messages.success(request, "Your Order has been completed. Thank you ")
            return render(request, 'core/order_complete.html', {
                'ordercode': ordercode,
                'category': category,
                'setting': setting,
            })
        else:  # на всякий случай вывод ошибок при валидации
            print('ОШИБКИ', form.errors)
            messages.warning(request, form.errors)
            return HttpResponseRedirect("/order/checkout/")
    else:
        print('НЕ ПОСТ ЗАПРОС !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

    context = {'category': category,
               'shopcart': shopcart,
               'setting': setting,
               'profile': profile,
               'total': int(total),
               'quantity': quantity,
               }
    return render(request, 'core/checkout.html', context)
