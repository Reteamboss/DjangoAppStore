# Generated by Django 3.2.5 on 2022-08-30 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_auto_20220823_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='first_name_customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='flat',
        ),
        migrations.RemoveField(
            model_name='order',
            name='house',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name_customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='order',
            name='street',
        ),
    ]