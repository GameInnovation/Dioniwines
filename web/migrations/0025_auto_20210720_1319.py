# Generated by Django 3.0.3 on 2021-07-20 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0024_auto_20210720_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeddback',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
