# Generated by Django 4.2.4 on 2023-08-20 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_options_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('set_active', 'Can deactivate user')], 'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активный'),
        ),
    ]
