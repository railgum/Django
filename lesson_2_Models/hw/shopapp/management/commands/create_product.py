from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
import random
from shopapp.models import Product


class Command(BaseCommand):
    help = 'Create products'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Product count')

    def handle(self, *args, **options):
        count = options.get('count')
        for i in range(1, count + 1):
            product = Product(
                title=lorem_ipsum.words(2, common=False).capitalize(),
                description="\n".join(lorem_ipsum.paragraphs(2, common=False)),
                price=round(random.randint(500, 5000) * random.random(), 2),
                quantity=random.randint(1, 10),
                add_date=f'{random.randint(2020, 2024)}-0{random.randint(1, 9)}-{random.randint(10, 28)}',
            )
            product.save()

