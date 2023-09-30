from django.contrib import admin
from .models import Category, Product, Images


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['title', 'description']


class ProductImagesInline(admin.TabularInline):
    model = Images
    extra = 5


class ProductAdmin(admin.ModelAdmin):
    list_filter = ['title', 'description']
    list_display = ['title', 'image_tag']
    inlines = (ProductImagesInline, )

class ImagesAdmin(admin.ModelAdmin):
    list_filter = ['title']
    list_display = ['title', 'product', 'image_tag']
    readonly_fields = ('image_tag',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Images, ImagesAdmin)
