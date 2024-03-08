from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('registration/', log_in, name='log_in'),
    path('orders/<int:user_id>/', client_all_orders, name='show_orders_clients'),
    path('orders_by_date/<int:client_id>', orders_by_date, name='show_orders_by_date'),
    path('change_product', input_product_id, name='input_product_id'),
    path('change_product/<int:product_id>/', change_product_form, name='change_product_form'),
]
