# Generated by Django 3.1.4 on 2021-02-08 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_message_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='like',
            new_name='like_id',
        ),
    ]