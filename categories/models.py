from django.db import models

# Create your models here.


class Category(models.Model):
    category_id = models.AutoField(primary_key=True, editable=False)
    category_name = models.CharField(max_length=40)
    description = models.CharField(max_length=40)

    def __str__(self):
        return "%s" % (self.category_name)
