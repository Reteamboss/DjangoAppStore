# Generated by Django 3.2.5 on 2022-08-23 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_alter_order_dateofdelivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='dateofdelivery',
            field=models.DateField(verbose_name='Дата доставки'),
        ),
    ]
