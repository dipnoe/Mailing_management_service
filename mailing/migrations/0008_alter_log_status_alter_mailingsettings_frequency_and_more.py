# Generated by Django 4.2.4 on 2023-08-18 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0007_alter_mailingsettings_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='status',
            field=models.CharField(choices=[('S', 'SUCCESSFUL'), ('UNS', 'UNSUCCESSFUL')], max_length=20, verbose_name='статус попытки'),
        ),
        migrations.AlterField(
            model_name='mailingsettings',
            name='frequency',
            field=models.CharField(choices=[('O', 'ONCE'), ('D', 'DAY'), ('W', 'WEEK'), ('M', 'MONTH')], max_length=10, verbose_name='периодичность'),
        ),
        migrations.AlterField(
            model_name='mailingsettings',
            name='status',
            field=models.CharField(choices=[('CR', 'CREATED'), ('LA', 'LAUNCHED'), ('CO', 'COMPLETED')], default='CR', max_length=15, verbose_name='статус рассылки'),
        ),
    ]
