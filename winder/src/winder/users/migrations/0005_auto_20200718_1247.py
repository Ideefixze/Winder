# Generated by Django 3.0.8 on 2020-07-18 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200718_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default='No bio.', max_length=300),
        ),
    ]
