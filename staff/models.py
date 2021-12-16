from django.db import models

# Create your models here.

class Role(models.Model):
    role_id = models.AutoField(primary_key=True, editable=False)
    role_name = models.CharField(max_length=40)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.role_name

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    address = models.CharField(max_length=256)
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=128)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_password)