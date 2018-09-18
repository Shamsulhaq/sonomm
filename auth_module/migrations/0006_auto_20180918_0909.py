# Generated by Django 2.1.1 on 2018-09-18 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0005_auto_20180918_0707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='image',
        ),
        migrations.AddField(
            model_name='customer',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='Customer/profile'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]