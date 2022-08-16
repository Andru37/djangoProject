from django.contrib import admin
from myfirstproject.models import ProductCategory, Product


class ProductModelsAdmin(admin.ModelAdmin):
    list_display = "product_n", "price_product", "amount_product", "in_stock"
    list_editable = "price_product", "amount_product"
    list_filter = "amount_product", "product_category", "in_stock"


admin.site.register(ProductCategory)
admin.site.register(Product, ProductModelsAdmin)
# Register your models here.



