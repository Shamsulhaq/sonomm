# Generated by Django 2.1 on 2018-09-13 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommarce', '0005_auto_20180913_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='productbasic',
            name='unit',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
