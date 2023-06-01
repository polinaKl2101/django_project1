from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'category_name': 'Продукты', 'category_desc': 'Молоко'},
            {'category_name': 'Вещи', 'category_desc': 'Джинсы'},
            {'category_name': 'Автомобили', 'category_desc': 'BMW'},
            {'category_name': 'Материал', 'category_desc': 'Железо'},
        ]

        Category.objects.all().delete()

        created_categories = []

        for category in category_list:
            created_categories.append(
                Category(**category)
            )

        Category.objects.bulk_create(created_categories)