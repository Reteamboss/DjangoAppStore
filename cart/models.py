from django.db import models

from account.models import User
from catalog.models import Product


class Order(models.Model):
    customer = models.ForeignKey(User, related_name='customer',
                                 on_delete=models.CASCADE, verbose_name='Покупатель')
    products = models.ManyToManyField(Product, verbose_name='Товары', blank=True, through='ProductsInOrder')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    paymentmethod = models.CharField( max_length=64, verbose_name='Cпособ оплаты',null=True)
    deliverytype = models.CharField( max_length=64, verbose_name='Cпособ доставки',null=True)
    address = models.CharField( max_length=64, verbose_name='Адрес доставки',null=True)
    phone = models.CharField( max_length=64, verbose_name='Номер телефона',null=True)
    dateofdelivery = models.DateField( verbose_name='Дата доставки',null=True)
    total_price = models.IntegerField(verbose_name='Общая цена', null=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.customer} - {self.created}'


class ProductsInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Товар', related_name='count_in_order',)
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество товара в заказе')
