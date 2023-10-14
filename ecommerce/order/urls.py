from django.urls import path, include

from .views import index, addtoshopcart, shopcart


urlpatterns = [
    path('', index, name='index'),
    path('addtoshopcart/<int:pk>/', addtoshopcart, name='addtoshopcart'),
    path('shopcart/', shopcart, name='shopcart')
]