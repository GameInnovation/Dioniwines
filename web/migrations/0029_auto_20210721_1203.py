# Generated by Django 3.0.3 on 2021-07-21 09:03

from django.db import migrations, models
import web.storage


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0028_auto_20210721_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeddback',
            name='customer_photo',
            field=models.ImageField(blank=True, null=True, storage=web.storage.OverwriteStorage(), upload_to='customer'),
        ),
    ]
