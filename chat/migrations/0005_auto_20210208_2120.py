# Generated by Django 3.1.4 on 2021-02-08 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20210208_2049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='like_id',
            new_name='like',
        ),
    ]
