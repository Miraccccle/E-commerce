from django.urls import path

from .views import index, category_products, product_detail, add_comments

app_name = 'product'

urlpatterns = [
    path('', index),
    path('category/<int:pk>/<slug:slug>/', category_products, name='category_products'),
    path('products/<int:pk>/<slug:slug>/', product_detail, name='detail'),
    path('product/add_comment/<int:pk>/', add_comments, name='add_comment'),
]