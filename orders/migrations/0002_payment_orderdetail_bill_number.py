# Generated by Django 4.0 on 2021-12-16 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('bill_number', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('payment_type', models.CharField(max_length=40)),
                ('order_detail_id', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='bill_number',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='orders.payment'),
        ),
    ]