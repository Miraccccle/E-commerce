from django.contrib import admin
from .models import Category, Product


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['title', 'description']


class ProductAdmin(admin.ModelAdmin):
    list_filter = ['title', 'description']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)