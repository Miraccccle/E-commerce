from django.urls import path, include

from .views import index, contact, cart, checkout, detail, shop, search, search_auto

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('cart/', cart, name='cart'),
    path('checkoout/', checkout, name='checkout'),
    path('shop/', shop, name='shop'),
    path('search/', search, name='search'),
    path('search_auto/', search_auto, name='search_auto'),
]