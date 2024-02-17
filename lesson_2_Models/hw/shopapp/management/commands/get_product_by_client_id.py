from django.core.management.base import BaseCommand
from shopapp.models import Order, Client, Product

class Command(BaseCommand):
    help = 'Get client products'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **options):
        pk = options.get('pk')
        client = Client.objects.filter(pk=pk).first()
        orders = Order.objects.filter(client_id=client.id).all()
        # products = Order.objects.filter(client_id=pk)
        # products = Product.objects.filter(id=orders.id=client.id))
        self.stdout.write(f'{orders}')

