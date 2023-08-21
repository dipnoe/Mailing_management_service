from django.core.mail import send_mail
from mailing.models import Message, Customer, Mailing, Log
from config import settings
from django.utils import timezone


def send_mailing(message: Message):
    emails = [customer.email for customer in Customer.objects.all()]

    current_time = timezone.now().time()

    if message.mailing.status == 'CR' and message.mailing.distribution_settings < current_time:

        try:
            send_mail(
                f'{message.title}',
                f'{message.body}',
                settings.EMAIL_HOST_USER,
                emails
            )
            log = Log.objects.create(last_try=current_time, status='S', response='успешно')


        except Exception as ex:
            log = Log.objects.create(last_try=current_time, status='UNS', response=str(ex))

        finally:
            if message.mailing.frequency == 'O':
                message.mailing.status = 'CO'
            else:
                message.mailing.status = 'LA'
            message.mailing.save()
            log.save()
