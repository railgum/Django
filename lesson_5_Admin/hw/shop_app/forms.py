from django import forms
from .models import Product


class ImageForm(forms.Form):
    image = forms.ImageField(label='Изображение')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['image']
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'price': 'Цена',
            'quantity': 'Количество',
            'add_date': 'Дата изменения',
        }
