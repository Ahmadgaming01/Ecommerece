# Generated by Django 4.2.3 on 2023-10-03 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_cartdetail_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdetail',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
