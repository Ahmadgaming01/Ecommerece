# Generated by Django 4.2.3 on 2023-09-27 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
    ]
