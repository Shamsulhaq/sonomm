# Generated by Django 2.1.1 on 2018-09-27 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommarce', '0031_auto_20180927_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_Method',
            field=models.CharField(blank=True, choices=[('o', 'Office Pick'), ('h', 'Home Delivery')], default=None, max_length=1, null=True),
        ),
    ]
