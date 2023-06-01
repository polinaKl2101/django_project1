from django.contrib import admin
from catalog.models import Category, Product

#admin.site.register(Category)
#admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'products_name', 'price_per_purchase', 'category')
    list_filter = ('category',)
    search_fields = ('products_name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)