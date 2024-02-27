from django.core.management.base import BaseCommand
from random import choice, randint
from django.db.models import Sum
from datetime import date, timedelta
from shop_app.models import Client, Product, Order


class Command(BaseCommand):
    help = 'Create order'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Client ID')

    def handle(self, *args, **options):
        products_ord = Product.objects.all()
        pk = options.get('id')
        order = Order(
            client_id=pk,
            order_date=date.today() - timedelta(randint(0, 3))
        )
        order.save()
        for _ in range(1, randint(1, 5)):
            order.products.add(choice(products_ord))
            amount = order.products.all().annotate(amount=Sum('price'))
            print(amount[0].amount)
            order.amount = amount[0].amount
        order.save()
