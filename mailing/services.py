from datetime import timedelta

from django.core.mail import send_mail
from mailing.models import Message, Customer, Mailing, Log
from config import settings
from django.utils import timezone

from dateutil.relativedelta import relativedelta

import logging


def mailing_job():
    print('mailing_job() started')
    messages = Message.objects.filter(mailing__status__in=['CR', 'LA'])
    for message in messages:
        print(message)
        send_mailing(message)


def get_next_mailing_time(mailing: Mailing):
    frequency = mailing.frequency
    if frequency == 'D':
        return mailing.last_mailing_time + timedelta(days=1)
    if frequency == 'W':
        return mailing.last_mailing_time + timedelta(days=7)
    if frequency == 'M':
        return mailing.last_mailing_time + relativedelta(month=+1)


def send_mailing(message: Message):
    emails = [customer.email for customer in Customer.objects.all()]

    current_datetime = timezone.now()
    current_time = current_datetime.time()

    if ((message.mailing.status == 'CR' and message.mailing.distribution_settings < current_time) or
            (message.mailing.status == 'LA' and message.mailing.last_mailing_time is None
             and message.mailing.distribution_settings < current_time) or
            (message.mailing.status == 'LA' and get_next_mailing_time(message.mailing) < current_datetime)):
        print(message.body)
        try:
            send_mail(
                f'{message.title}',
                f'{message.body}',
                settings.EMAIL_HOST_USER,
                emails
            )
            print('сообщение отправлено')
            log = Log.objects.create(
                last_try=current_time,
                status='S', response='успешно',
                mailing_settings=message.mailing
            )
            message.mailing.last_mailing_time = timezone.now()

        except Exception as ex:
            log = Log.objects.create(
                last_try=current_time,
                status='UNS',
                response=str(ex),
                mailing_settings=message.mailing
            )

        finally:
            if message.mailing.frequency == 'O':
                message.mailing.status = 'CO'
            else:
                message.mailing.status = 'LA'
            message.mailing.save()
            log.save()
