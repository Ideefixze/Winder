# Generated by Django 3.0.8 on 2020-07-17 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200717_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='profile_pictures/nophoto.png', upload_to='profile_pictures'),
        ),
    ]
