from django.urls import path, include

from .views import index, contact, cart, checkout, detail, shop

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('cart/', cart, name='cart'),
    path('checkoout/', checkout, name='checkout'),
    # path('shop/', shop, name='shop'),
    path('category/', include('product.urls'), name='shop'),
    path('product/', include('product.urls'), name='product'),
]