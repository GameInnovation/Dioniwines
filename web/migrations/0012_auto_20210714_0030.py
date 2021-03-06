# Generated by Django 3.0.3 on 2021-07-13 21:30

from django.db import migrations, models
import web.storage


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_remove_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, storage=web.storage.OverwriteStorage.get_available_name, upload_to='images'),
        ),
    ]
