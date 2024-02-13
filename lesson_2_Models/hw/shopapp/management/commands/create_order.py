from django.core.management.base import BaseCommand
from shopapp.models import Client, Product, Order
from random import choice, randint

class Command(BaseCommand):
    help = 'Create orders'

    def handle(self, *args, **options):
        clients = Client.objects.all()
        products = Product.objects.all()

        for _ in range(10):
            customer = choice(clients)
            product = choice(products)
            amount =