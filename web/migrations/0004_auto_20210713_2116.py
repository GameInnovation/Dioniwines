# Generated by Django 3.0.3 on 2021-07-13 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20210713_2045'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ImageForExtractText',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
