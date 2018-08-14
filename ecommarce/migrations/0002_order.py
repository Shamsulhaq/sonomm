# Generated by Django 2.1 on 2018-08-14 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0001_initial'),
        ('ecommarce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quentity', models.PositiveIntegerField(default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('payment_Status', models.BooleanField(default=False)),
                ('coustomer_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=14)),
                ('delivery_Address', models.CharField(max_length=1000)),
                ('delivery_status', models.BooleanField(default=False)),
                ('delivery_Area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_module.Area')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommarce.ProductBasic')),
            ],
            options={
                'ordering': ['-updated', '-timestamp'],
            },
        ),
    ]