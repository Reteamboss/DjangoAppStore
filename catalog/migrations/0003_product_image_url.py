# Generated by Django 3.2.5 on 2022-08-23 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.CharField(max_length=255, null=True, verbose_name='Адрес картинки'),
        ),
    ]