# Generated by Django 4.2.4 on 2023-08-20 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0024_alter_mailingsettings_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailingsettings',
            name='mailing',
        ),
        migrations.AddField(
            model_name='mailing',
            name='mailing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingsettings', verbose_name='рассылка'),
        ),
    ]
