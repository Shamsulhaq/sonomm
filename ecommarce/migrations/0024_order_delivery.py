# Generated by Django 2.1.1 on 2018-09-27 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommarce', '0023_auto_20180926_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.CharField(choices=[('o', 'Office Pick'), ('h', 'Home Delivery')], default=None, max_length=1),
        ),
    ]