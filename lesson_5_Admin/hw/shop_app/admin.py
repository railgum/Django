from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Client, Product, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    list_filter = ['name', 'reg_date', ]
    search_fields = ['name']
    fieldsets = [
        (
            'Основная информация', {
                'fields': ['name', 'reg_date'],
                'description': 'Основная информация',
            }
        ),
        (
            'Дополнительная информация', {
                'fields': ['email', 'phone', 'address'],
                'classes': ['wide', 'collapse'],
                'description': 'Дополнительная информация',
            }
        )
    ]


@admin.action(description='Обнулить количество')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'quantity', 'price', 'get_photo', ]
    list_filter = ['add_date', ]
    search_fields = ['description']
    actions = [reset_quantity]
    fieldsets = [
        (
            'Основная информация', {
                'fields': ['title', 'quantity'],
            }
        ),
        (
            'Дополнительная информация', {
                'fields': ['price', 'description', 'add_date'],
                'classes': ['wide', 'collapse'],
            }
        )
    ]

    def get_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")
        else:
            return "Нет фото"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_date', 'amount']
    search_fields = ['order_date']
    fieldsets = [
        (
            'Основная информация', {
                'fields': ['order_date', 'amount'],
            }
        ),
    ]
