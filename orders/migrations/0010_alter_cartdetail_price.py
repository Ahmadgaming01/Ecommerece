# Generated by Django 4.2.3 on 2023-10-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_cart_coupon_cart_total_with_coupon_order_coupon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetail',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]