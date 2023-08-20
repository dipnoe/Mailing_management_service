# Generated by Django 4.2.4 on 2023-08-20 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0030_remove_message_mailing_mailing_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='message',
        ),
        migrations.AddField(
            model_name='message',
            name='mailing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailing.mailing', verbose_name='рассылка'),
        ),
    ]
