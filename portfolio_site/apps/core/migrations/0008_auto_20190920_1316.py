# Generated by Django 2.2.5 on 2019-09-20 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190920_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/'),
        ),
    ]