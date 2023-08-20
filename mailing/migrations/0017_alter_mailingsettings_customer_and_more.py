# Generated by Django 4.2.4 on 2023-08-20 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailing', '0016_alter_mailingsettings_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingsettings',
            name='customer',
            field=models.ManyToManyField(to='mailing.customer', verbose_name='клиент'),
        ),
        migrations.AlterField(
            model_name='mailingsettings',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='владелец рассылки'),
        ),
    ]
