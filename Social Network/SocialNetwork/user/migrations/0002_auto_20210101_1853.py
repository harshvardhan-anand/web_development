# Generated by Django 3.1.4 on 2021-01-01 13:23

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=user.models.get_image_file_path),
        ),
    ]
