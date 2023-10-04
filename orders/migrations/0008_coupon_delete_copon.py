# Generated by Django 4.2.3 on 2023-10-04 09:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_cartdetail_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25)),
                ('percentage', models.FloatField()),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Copon',
        ),
    ]
