# Generated by Django 2.1.1 on 2018-09-27 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommarce', '0029_auto_20180927_0340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_on_process',
        ),
    ]
