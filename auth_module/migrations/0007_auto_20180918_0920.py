# Generated by Django 2.1.1 on 2018-09-18 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommarce', '0014_remove_order_delivery_area'),
        ('auth_module', '0006_auto_20180918_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='area',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.DeleteModel(
            name='Area',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
