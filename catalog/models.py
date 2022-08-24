from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):

    name = models.CharField(
        max_length=255,
        verbose_name='Категория',
    )

    slug = models.SlugField(unique=True)

    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Каталог',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('-id',)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'catalog:product_list_by_category',
            kwargs={'category_slug': self.slug}
        )
    # def get_absolute_url(self):
    #     return reverse(
    #         'catalog:products',
    #         kwargs={'category_slug': self.slug})

class Color(models.Model):
    color = models.CharField(
        max_length=255,
        verbose_name='Цвет',
    )
    def __str__(self):
        return str(self.color)

class Display(models.Model):
    display = models.FloatField(
        verbose_name='Диагональ',
    )

    def __str__(self):
        return str(self.display)

class Memory(models.Model):
    memory = models.IntegerField(
        verbose_name='Память',
    )

    def __str__(self):
        return str(self.memory)


class Product(models.Model):

    title = models.CharField(
        max_length=255,
        verbose_name='Наименование',
    )

    price = models.DecimalField(
        max_digits=19,
        decimal_places=0,
        verbose_name='Цена',

    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name='Категория',
    )

    description = models.TextField(verbose_name='Описание')

    image = models.ImageField(
        upload_to='catalog/',
        verbose_name='Изображение',
    )

    image_url = models.CharField(
        max_length=255,
        verbose_name='Адрес картинки',
        null=True,
    )

    memory = models.ForeignKey(
        Memory,
        on_delete=models.PROTECT,
        verbose_name='Память',
    )

    color = models.ForeignKey(
        Color,
        on_delete=models.CASCADE,
        verbose_name='Цвет',
    )

    display = models.ForeignKey(
        Display,
        on_delete=models.PROTECT,
        verbose_name='Диагональ',
    )


    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'catalog:product_detail',
            kwargs={
                'product_slug': self.slug,
                'category_slug': self.category.slug
            }
        )

    # def get_absolute_url(self):
    #     return reverse('product-detail',args=[str(self.id)])


class Review(models.Model):

    product = models.ForeignKey(
        Product,
        related_name='reviews',
        on_delete=models.PROTECT,
        verbose_name='Товар'
    )

    name = models.CharField(
        max_length=64,
        verbose_name='Имя',
    )

    rating = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг'
    )
    review = models.TextField(
        max_length=255,
        verbose_name='Отзыв'
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name


class Quantity(models.Model):

    product = models.ForeignKey(
        Product,
        related_name='quantity',
        on_delete=models.PROTECT,
        verbose_name='Количество'
    )

    quantity = models.IntegerField(
        verbose_name='Количество'
    )

    def __str__(self):
        return str(self.product)



