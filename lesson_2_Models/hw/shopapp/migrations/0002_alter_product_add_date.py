# Generated by Django 5.0.1 on 2024-02-12 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='add_date',
            field=models.DateField(),
        ),
    ]
