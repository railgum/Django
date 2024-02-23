from django.core.management.base import BaseCommand
from shop_template_app.models import Client

class Command(BaseCommand):
    help = 'Update clients'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('email', type=str, help='New email')

    def handle(self, *args, **options):
        pk = options.get('pk')
        email = options.get('email')
        client = Client.objects.filter(pk=pk).first()
        client.email = email
        client.save()
        self.stdout.write(f'{client}')
