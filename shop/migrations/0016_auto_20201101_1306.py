# Generated by Django 3.1.2 on 2020-11-01 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20201101_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='payment_id',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
