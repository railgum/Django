from django.core.management.base import BaseCommand
from shopapp.models import Client, Product, Order
from random import choice, randint
from django.db.models import Sum


class Command(BaseCommand):
    help = 'Create orders'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Client ID')

    def handle(self, *args, **options):
        products = Product.objects.all()
        pk = options.get('id')
        order = Order(
            client_id=pk,
            amount=100,
        )
        print(products.filter(pk=order.products).aggregate(Sum('price')))
        order.save()
        # amount = 0
        for _ in range(1, randint(1, 5)):
            order.products_id.add(choice(products.pk))
            self.stdout.write(order)
            # amount += order.products.price
        # order.amount = products.filter(pk=order.products_id).aggregate(Sum('price'))
        order.save()
