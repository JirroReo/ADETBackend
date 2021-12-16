from django.db import models
from supplier.models import Supplier
from categories.models import Category

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True, editable=False)
    product_name = models.CharField(max_length=40)
    product_description = models.CharField(blank=True, max_length=40)
    product_unit = models.CharField(blank=True, max_length=40)
    product_price = models.DecimalField(decimal_places=2, max_digits=10)
    product_quantity = models.IntegerField(default=0)
    product_status = models.IntegerField(default=0)
    other_details = models.CharField(max_length=256, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.product_name)