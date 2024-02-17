from django.core.management.base import BaseCommand
from shopapp.models import Client, Product, Order
from random import choice, randint
from django.db.models import Sum


class Command(BaseCommand):
    help = 'Create orders'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Client ID')

    def handle(self, *args, **options):
        products_ord = Product.objects.all()
        pk = options.get('id')
        order = Order(
            client_id=pk,
        )
        order.save()
        for _ in range(1, randint(1, 5)):
            order.products.add(choice(products_ord))
        # amount = order.products.all().aggregate(Sum('price'))
        amount = order.products.all().annotate(amount=Sum('price'))
        print(amount[0].amount)
        order.amount = amount[0].amount
        order.save()
