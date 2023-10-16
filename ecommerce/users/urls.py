from django.urls import path
from .views import index, logout_func, login_func, register_func

urlpatterns = [
    path('', index, name='user_index'),
    path('login/', login_func, name='login'),
    path('logout/', logout_func, name='logout'),
    path('register/', register_func, name='register'),
]