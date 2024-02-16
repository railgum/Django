from django.core.management.base import BaseCommand
from shopapp.models import Client, Product, Order
from random import choice, randint


class Command(BaseCommand):
    help = 'Create orders'
    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Client ID')

    def handle(self, *args, **options):
        products = Product.objects.all()
        pk = options.get('id')
        order = Order.objects.create(client_id=pk)
        amount = 0
        for _ in range(1, randint(1, 5)):
            order.product_set.add(choice(products))
            self.stdout.write(order.product.price)
            amount += order.product.price
        order.amount = amount
        order.save()
