# Generated by Django 3.0.8 on 2020-07-14 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lovematch', '0004_user_group'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('question', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('nickname', 'group')},
        ),
    ]
