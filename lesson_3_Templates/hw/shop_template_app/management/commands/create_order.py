from django.core.management.base import BaseCommand
from random import choice, randint
from django.db.models import Sum
from shop_template_app.models import Client, Product, Order



class Command(BaseCommand):
    help = 'Create orders'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count orders')

    def handle(self, *args, **options):
        products_ord = Product.objects.all()
        count = options.get('count')
        for i in range(1, count + 1):
            order = Order(
                client_id=randint(1, Client.objects.count()),
                order_date=f'{randint(2022, 2023)}-0{randint(1, 9)}-{randint(10, 28)}',
            )
            order.save()
            for _ in range(1, randint(1, 5)):
                order.products.add(choice(products_ord))
                amount = order.products.all().annotate(amount=Sum('price'))
                print(amount[0].amount)
                order.amount = amount[0].amount
            order.save()
