# Generated by Django 3.1.5 on 2021-01-05 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='user_like_count',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
    ]
