from django.core.validators import MinValueValidator
from django.db import models


class ProductCategory(models.Model):

    product_name = models.CharField(max_length=32)
    unique_name = models.SlugField(null=True)
    number_of_species = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)
# Create your models here.


class Product(models.Model):

    product_n = models.CharField(max_length=32)
    price_product = models.IntegerField(null=True, validators=[MinValueValidator(0)])
    amount_product = models.IntegerField(null=True, validators=[MinValueValidator(0)])
    description = models.TextField(null=True, blank=True)
    product_category = models.ForeignKey(ProductCategory,
                                         on_delete=models.CASCADE,
                                         related_name='product')
