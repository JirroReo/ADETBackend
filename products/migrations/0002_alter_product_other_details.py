# Generated by Django 4.0 on 2021-12-15 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='other_details',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
