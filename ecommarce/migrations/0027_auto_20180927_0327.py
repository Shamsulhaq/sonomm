# Generated by Django 2.1.1 on 2018-09-27 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommarce', '0026_auto_20180927_0326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='delivery_method',
            new_name='delivery_Method',
        ),
    ]
