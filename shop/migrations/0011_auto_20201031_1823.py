# Generated by Django 3.1.2 on 2020-10-31 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_cart_quatity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='quatity',
            new_name='quantity',
        ),
    ]