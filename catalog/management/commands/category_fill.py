from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'category_name': 'Продукты', 'category_desc': 'еда'},
            {'category_name': 'Вещи', 'category_desc': 'одежда'},
            {'category_name': 'Автомобили', 'category_desc': 'машины'},
            {'category_name': 'Материал', 'category_desc': 'вещества'},
        ]

        Category.objects.all().delete()

        created_categories = []

        for category in category_list:
            created_categories.append(
                Category(**category)
            )

        Category.objects.bulk_create(created_categories)