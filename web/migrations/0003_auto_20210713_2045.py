# Generated by Django 3.0.3 on 2021-07-13 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_image_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageForExtractText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
    ]