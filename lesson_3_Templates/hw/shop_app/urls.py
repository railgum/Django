from django.urls import path
from .views import *

urlpatterns = [
    path('orders/<int:user_id>/', client_all_orders, name='show_orders_clients'),
    path('orders_by_date/<int:client_id>', orders_by_date, name='show_orders_by_date'),
]
