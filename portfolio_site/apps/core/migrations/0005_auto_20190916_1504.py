# Generated by Django 2.2.5 on 2019-09-16 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190911_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='media/pictures'),
        ),
    ]