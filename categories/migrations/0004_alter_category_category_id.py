# Generated by Django 4.0 on 2021-12-15 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_alter_category_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
