# Generated by Django 3.0.3 on 2021-07-28 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0032_auto_20210725_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feeddback',
            old_name='delete',
            new_name='deleted',
        ),
    ]