# import datetime
#
# from django.core.mail import send_mail
#
# from mailing.models import Message, Customer, Mailing, Log
# from config import settings
#
#
# def send_mailing(message: Message, mailing: Mailing):
#     emails = []
#     for customer in Customer.objects.all():
#         emails.append(str(customer.email))
#
#     if (mailing.frequency == 'O' and
#             datetime.datetime.fromisoformat(mailing.distribution_settings) <= datetime.datetime.now()):
#         try:
#             send_mail(
#                 f'{message.title}',
#                 f'{message.body}',
#                 settings.EMAIL_HOST_USER,
#                 [*emails]
#             )
#             log = Log.objects.create(last_try=datetime.datetime.now(), status='S', response='успешно')
#             log.save()
#             mailing.status = 'CO'
#             mailing.save()
#
#         except Exception as ex:
#             log = Log.objects.create(last_try=datetime.datetime.now(), status='UNS', response=ex)
#             log.save()
#     else:
#         mailing.status = 'LA'
#         mailing.save()

from django.core.mail import send_mail
from mailing.models import Message, Customer, Mailing, Log
from config import settings
from django.utils import timezone


def send_mailing(message: Message):
    emails = [customer.email for customer in Customer.objects.all()]

    current_time = timezone.now().time()

    if (message.mailing.frequency == 'O' and
            message.mailing.distribution_settings <= current_time):

        try:
            send_mail(
                f'{message.title}',
                f'{message.body}',
                settings.EMAIL_HOST_USER,
                emails
            )
            log = Log.objects.create(last_try=current_time, status='S', response='успешно')
            print(message.mailing.status)
            message.mailing.status = 'CO'
            message.mailing.save()

        except Exception as ex:
            log = Log.objects.create(last_try=current_time, status='UNS', response=str(ex))

        finally:
            log.save()

    else:
        message.mailing.status = 'LA'
        message.mailing.save()
