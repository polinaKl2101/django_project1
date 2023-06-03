from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        autos = Category.objects.get(category_name='Автомобили')
        products = Category.objects.get(category_name='Продукты')
        goods = Category.objects.get(category_name='Вещи')
        materials = Category.objects.get(category_name='Материал')

        products_list = [
            {'products_name': 'BMW', 'product_image': 'prod_images/bmw.jpg' , 'description': 'white', 'category': autos, 'price_per_purchase': 5000000},
            {'products_name': 'Milk', 'description': 'coconut', 'category': products, 'price_per_purchase': 50},
            {'products_name': 'Jeans', 'description': 'levis', 'category': goods, 'price_per_purchase': 3579},
            {'products_name': 'Gold', 'description': 'gold', 'category': materials, 'price_per_purchase': 6666666},
        ]

        Product.objects.all().delete()

        created_products = []

        for product in products_list:
            created_products.append(
                Product(**product)
            )

        Product.objects.bulk_create(created_products)