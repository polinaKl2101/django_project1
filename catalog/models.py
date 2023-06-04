from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    products_name = models.CharField(max_length=100, verbose_name='имя продукта')
    description = models.CharField(max_length=500, verbose_name='описание',  **NULLABLE)
    product_image = models.ImageField(upload_to='prod_images/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=500, verbose_name='Категория')
    price_per_purchase = models.IntegerField(verbose_name='цена за покупку')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    last_time_modified = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f"Название: {self.products_name}. " \
               f"Категория: {self.category}. " \
               f"Цена: {self.price_per_purchase}. " \
               f"Дата публикации: {self.date_created}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='наименование категории')
    category_desc = models.CharField(max_length=250, verbose_name='описание',  **NULLABLE)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'