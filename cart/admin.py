from django.contrib import admin

from .models import Order, ProductsInOrder


class ProductsInOrderInline(admin.TabularInline):
    model = ProductsInOrder

    verbose_name = 'Заказанный товар'
    verbose_name_plural = 'Заказанные товары'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ordering = ('created',)
    list_display = ('id','first_name_customer','last_name_customer','customer','total_price', 'created','address','phone')

    inlines = (ProductsInOrderInline,)

    def quantity(self, obj):
        return ProductsInOrder.objects.filter(order=obj).count()

    quantity.short_description = 'Количество позиций'

