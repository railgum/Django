from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
from .models import Client, Product, Order
from datetime import date, timedelta
from .forms import *


def index(request):
    context = {"name": "Rail"}
    return render(request, "shop_app/index.html", context)


def shop(request):
    products = Product.objects.all()
    context = {"title": "Эластико",
               "products": products, }
    return render(request, "shop_app/elastico.html", context)


# def add_client_form(request):
#     clients =

def log_in(request):
    # registration form
    pass


def client_all_orders(request, user_id):
    client = get_object_or_404(Client, pk=user_id)
    orders = Order.objects.filter(client_id=client.id)
    # products_dict = {}
    products_list = []

    for order in orders:
        products_list.append(order.products.values_list("title"))
    return render(
        request,
        'shop_app/show_orders.html',
        {'client': client, 'pl': products_list, 'orders': orders}
    )


def orders_by_date(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client_id=client.id)
    today = date.today()
    seven_day_before = today - timedelta(days=7)
    month_before = today - timedelta(days=31)
    year_before = today - timedelta(days=365)

    orders_last_week = orders.filter(order_date__gte=seven_day_before)
    orders_last_month = orders.filter(order_date__gte=month_before)
    orders_last_year = orders.filter(order_date__gte=year_before)

    products_last_week = orders_last_week.values_list("products__title")
    products_last_month = orders_last_month.values_list("products__title")
    products_last_year = orders_last_year.values_list("products__title")
    return render(
        request,
        'shop_app/orders_by_date.html',
        {
            'orders_week': set(products_last_week),
            'orders_month': set(products_last_month),
            'orders_year': set(products_last_year),
        }
    )


def change_product_form(request, product_id):
    alter_product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product_form = ProductForm(request.POST, instance=alter_product)
        image_form = ImageForm(request.POST, request.FILES)
        if product_form.is_valid() and image_form.is_valid():
            alter_product = product_form.save()
            image = image_form.cleaned_data['image']
            FileSystemStorage().save(image.name, image)

            alter_product.image = image
            alter_product.save()

            return redirect('index')
    else:
        product_form = ProductForm(instance=alter_product)
        image_form = ImageForm()

    return render(
        request,
        'shop_app/product_form.html',
        {
            'alter_product': alter_product,
            'product_form': product_form,
            'image_form': image_form,
        }
    )

# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = form.cleaned_data['image']
#             fs = FileSystemStorage()
#             fs.save(image.name, image)
#     else:
#         form = ImageForm()
#     return render(
#         request,
#         'shop_app/product_form.html',
#         {
#             'image_form': form,
#         }
#     )


# class ProductFormChange(TemplateView):
#     template_name = 'product_form.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['product_form'] = ProductForm()
#         context['image_form'] = ImageForm()
#         return context
#
#     def post(self, request, *args, **kwargs):
#         product_form = ProductForm(request.POST)
#         image_form = ImageForm(request.POST, request.FILES)
#
#         if product_form.is_valid() and image_form.is_valid():
