# Generated by Django 3.2.9 on 2022-01-21 13:36

import animals.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0003_auto_20211202_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalone',
            name='cover',
            field=models.ImageField(null=True, upload_to=animals.models.user_directory_path, verbose_name='Основное изображение'),
        ),
    ]
