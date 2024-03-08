from django.core.management.base import BaseCommand
from random import choice, randint
from django.utils import lorem_ipsum
from shop_app.models import Client


class Command(BaseCommand):
    help = 'Create clients'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client count')

    def handle(self, *args, **options):
        count = options.get('count')
        for i in range(1, count + 1):
            client = Client(
                name=f'Name{i}',
                email=f'name{i}@mail.mail',
                phone=f'8-{randint(100, 999)}{randint(100, 999)}{randint(1000, 9999)}',
                address=lorem_ipsum.words(5, common=False).capitalize(),
                reg_date=f'2020-{randint(0, 1)}{randint(1, 2)}-{randint(10, 28)}',
            )
            client.save()
            self.stdout.write(f'{client.name}')
