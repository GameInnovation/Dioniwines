# Generated by Django 3.0.3 on 2021-07-20 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import web.storage


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0022_auto_20210720_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeddback',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='feeddback',
            name='datecompleted',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='feeddback',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='feeddback',
            name='customer_photo',
            field=models.ImageField(blank=True, storage=web.storage.OverwriteStorage(), upload_to='customer'),
        ),
        migrations.AlterField(
            model_name='feeddback',
            name='feedback',
            field=models.TextField(max_length=1000),
        ),
    ]
