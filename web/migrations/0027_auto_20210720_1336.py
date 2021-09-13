# Generated by Django 3.0.3 on 2021-07-20 10:36

from django.db import migrations, models
import web.storage


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0026_auto_20210720_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeddback',
            name='customer_photo',
            field=models.ImageField(blank=True, null=True, storage=web.storage.OverwriteStorage(), upload_to='customer'),
        ),
    ]
