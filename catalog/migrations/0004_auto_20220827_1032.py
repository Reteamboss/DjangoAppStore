# Generated by Django 3.2.5 on 2022-08-27 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_product_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(null=True, verbose_name='В наличии'),
        ),
        migrations.DeleteModel(
            name='Quantity',
        ),
    ]
