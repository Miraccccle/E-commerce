from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Category, Product, Images, Comment


# Register your models here.

class ProductImagesInline(admin.TabularInline):
    model = Images
    extra = 5


class ProductAdmin(admin.ModelAdmin):
    list_filter = ['title', 'description']
    list_display = ['title', 'image_tag']
    inlines = (ProductImagesInline,)
    prepopulated_fields = {'slug': ('title', ) }


class ImagesAdmin(admin.ModelAdmin):
    list_filter = ['title']
    list_display = ['title', 'product', 'image_tag']
    readonly_fields = ('image_tag',)


class CommentAdmin(admin.ModelAdmin):
    list_filter = ['rate', 'status', 'user', 'text', 'ip']
    list_display = ['product', 'subject', 'rate', 'status']
    readonly_fields = ['product', 'subject', 'rate', 'text', 'user', 'ip']


admin.site.register(Comment, CommentAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        'title',
        'description',
        # 'children_count'
    ),
    list_display_links=(
        'indented_title',
    ),
    prepopulated_fields={'slug': ('title', )},
    list_filter=('status', 'parent')
)
admin.site.register(Images, ImagesAdmin)
