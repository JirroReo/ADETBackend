from django.db import models
from customers.models import Customer
from products.models import Product

# Create your models here.

class Payment(models.Model):
    bill_number = models.AutoField(primary_key=True, editable=False)
    payment_type = models.CharField(max_length=40)
    order_detail_id = models.CharField(max_length=256)

    def __str__(self):
        return "%s for %s" % (self.bill_number, self.order_detail_id)

class OrderDetail(models.Model):
    order_detail_id = models.AutoField(primary_key=True, editable=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_price = models.DecimalField(decimal_places=2, max_digits=10)
    size = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(default=1)
    discount = models.IntegerField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    bill_number = models.ForeignKey(Payment, on_delete=models.CASCADE, default=0)

    @property
    def total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return "%s: %s" % (self.order_detail_id, self.product_id)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True, editable=False)
    date_of_order = models.DateField(auto_now_add=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_detail = models.ManyToManyField(OrderDetail)

    def __str__(self):
        return "%s %s" % (self.date_of_order, self.customer_id)