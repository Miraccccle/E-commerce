from django.contrib import admin
from .models import ShopCart


# Register your models here.


class ShopCartAdmin(admin.ModelAdmin):
    list_filter = ['product', 'user']
    list_display = ['product', 'user', 'quantity', 'price', 'amount']


admin.site.register(ShopCart, ShopCartAdmin)
