from django.db import models

# Create your models here.


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    phone = models.IntegerField(blank=True, null=True)
    fax = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True, max_length=40)
    other_details = models.CharField(max_length=256)

    def __str__(self):
        return "%s %s" % (self.supplier_id, self.name)