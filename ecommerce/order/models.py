from django.contrib.auth.models import User
from django.db import models

from product.models import Product


# Create your models here.


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    @property
    def price(self):
        return self.product.price

    @property
    def amount(self):
        return self.quantity * self.price

    def __str__(self):
        return f'ShopCart. User: {self.user}, product: {self.product}: {self.quantity}'
