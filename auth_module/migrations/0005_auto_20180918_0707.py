# Generated by Django 2.1.1 on 2018-09-18 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0004_auto_20180918_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(null=True, upload_to='customer/profile'),
        ),
    ]
