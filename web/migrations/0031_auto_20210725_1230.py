# Generated by Django 3.0.3 on 2021-07-25 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0030_feeddback_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeddback',
            name='feedback_description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='feeddback',
            name='deleted',
            field=models.BooleanField(),
        ),
    ]
