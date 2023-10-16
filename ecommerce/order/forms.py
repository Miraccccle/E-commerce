from .models import ShopCart, Order
from django.forms import ModelForm


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name','email','address','phone','city','country']

class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']
