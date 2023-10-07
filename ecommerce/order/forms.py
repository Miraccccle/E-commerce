from .models import ShopCart
from django.forms import ModelForm


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']
