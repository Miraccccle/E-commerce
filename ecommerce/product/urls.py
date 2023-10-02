from django.urls import path

from .views import index, category_products

app_name = 'product'

urlpatterns = [
    path('', index, name='detail'),
    path('<int:pk>/<slug:slug>/', category_products,name='category_products')
]