# Generated by Django 4.2.4 on 2023-08-19 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0009_mailingsettings_is_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingsettings',
            name='is_block',
            field=models.BooleanField(default=False, verbose_name='заблокирована'),
        ),
    ]
