from django.urls import path

from .views import index

app_name = 'product'

urlpatterns = [
    path('', index, name='product_index')
]