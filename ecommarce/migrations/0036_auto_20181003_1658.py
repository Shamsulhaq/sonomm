# Generated by Django 2.1.1 on 2018-10-03 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommarce', '0035_auto_20181003_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inspiringremark',
            old_name='activ',
            new_name='active',
        ),
    ]
