# Generated by Django 3.0.8 on 2020-07-14 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lovematch', '0003_auto_20200714_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.CharField(default='default', max_length=50),
            preserve_default=False,
        ),
    ]