# Generated by Django 2.1 on 2018-09-15 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommarce', '0006_productbasic_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='category/main'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(blank=True, upload_to='category/sub'),
        ),
    ]
