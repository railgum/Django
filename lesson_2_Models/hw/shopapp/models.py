from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    reg_date = models.DateField()

    def __str__(self):
        return f'Client name: {self.name}, email: {self.email}'


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    add_date = models.DateField()

    def __str__(self):
        return f'Product title: {self.title}, price: {self.price}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
