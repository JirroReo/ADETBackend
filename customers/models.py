from django.db import models
from staff.models import Staff
# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    address = models.CharField(max_length=256, blank=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)