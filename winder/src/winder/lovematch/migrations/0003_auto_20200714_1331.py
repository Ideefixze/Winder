# Generated by Django 3.0.8 on 2020-07-14 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lovematch', '0002_auto_20200714_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answerval',
            new_name='answer',
        ),
    ]
