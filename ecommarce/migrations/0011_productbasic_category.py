# Generated by Django 2.1.1 on 2018-09-17 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommarce', '0010_remove_productbasic_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='productbasic',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ecommarce.SubCategory'),
            preserve_default=False,
        ),
    ]
