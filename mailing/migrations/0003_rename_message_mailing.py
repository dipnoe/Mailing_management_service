# Generated by Django 4.2.4 on 2023-08-13 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_message_remove_mailingsettings_mailing_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='Mailing',
        ),
    ]
