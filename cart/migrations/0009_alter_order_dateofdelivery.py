# Generated by Django 3.2.5 on 2022-08-23 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_auto_20220823_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='dateofdelivery',
            field=models.DateField(null=True, verbose_name='Дата доставки'),
        ),
    ]
