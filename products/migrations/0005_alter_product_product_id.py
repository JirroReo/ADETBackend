# Generated by Django 4.0 on 2021-12-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
