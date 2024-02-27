from django.core.management.base import BaseCommand
from shop_app.models import Order, Client, Product

class Command(BaseCommand):
    help = 'Get client products'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **options):
        pk = options.get('pk')
        client = Client.objects.filter(pk=pk).first()
        orders = Order.objects.filter(client_id=client.id).all()
        products_order_id = []
        for order in orders:
            products_order_id.append(order.products.all().values("title"))
        self.stdout.write(f'{products_order_id}')
