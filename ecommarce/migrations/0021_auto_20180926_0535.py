# Generated by Django 2.1.1 on 2018-09-26 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommarce', '0020_productbasic_is_out_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productbasic',
            name='regular_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
    ]
