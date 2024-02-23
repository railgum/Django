# Создайте шаблон для вывода всех заказов клиента и
# списком товаров внутри каждого заказа.
# Подготовьте необходимый маршрут и представление.
# Создайте шаблон, который выводит список заказанных
# клиентом товаров из всех его заказов с сортировкой по времени:
# ○ за последние 7 дней (неделю)
# ○ за последние 30 дней (месяц)
# ○ за последние 365 дней (год)
# *Товары в списке не должны повторятся.

from django.shortcuts import render, get_object_or_404
from .models import Client, Product, Order
from datetime import date, timedelta


def client_all_orders(request, user_id):
    client = get_object_or_404(Client, pk=user_id)
    orders = Order.objects.filter(client_id=client.id)
    # products_dict = {}
    products_list = []

    for order in orders:
        products_list.append(order.products.values_list("title"))
    return render(
        request,
        'shop_template_app/show_orders.html',
        {'client': client, 'pl': products_list, 'orders': orders}
    )


def orders_by_date(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client_id=client.id)
    today = date.today()
    seven_day_before = today - timedelta(days=7)
    month_before = today - timedelta(days=31)
    year_before = today - timedelta(days=365)

    orders_last_week = orders.filter(order_date__gte=seven_day_before)
    orders_last_month = orders.filter(order_date__gte=month_before)
    orders_last_year = orders.filter(order_date__gte=year_before)

    products_last_week = orders_last_week.values_list("products__title")
    products_last_month = orders_last_month.values_list("products__title")
    products_last_year = orders_last_year.values_list("products__title")
    return render(
        request,
        'shop_template_app/orders_by_date.html',
        {
            'orders_week': set(products_last_week),
            'orders_month': set(products_last_month),
            'orders_year': set(products_last_year),
        }
    )
