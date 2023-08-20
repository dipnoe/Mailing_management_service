from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Customer(models.Model):
    email = models.EmailField(max_length=150, verbose_name='почта', unique=True)
    first_name = models.CharField(max_length=150, verbose_name='имя', **NULLABLE)
    last_name = models.CharField(max_length=150, verbose_name='фамилия', **NULLABLE)
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.last_name} ({self.email})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Mailing(models.Model):
    FREQUENCY_CHOICES = [
        ('O', 'ONCE'),
        ('D', 'DAY'),
        ('W', 'WEEK'),
        ('M', 'MONTH'),
    ]

    STATUS_CHOICES = [
        ('CR', 'CREATED'),
        ('LA', 'LAUNCHED'),
        ('CO', 'COMPLETED'),
    ]
    distribution_settings = models.TimeField(verbose_name='время рассылки', default='10:00')
    frequency = models.CharField(max_length=10, verbose_name='периодичность', choices=FREQUENCY_CHOICES, default='O')
    status = models.CharField(max_length=15, verbose_name='статус рассылки', choices=STATUS_CHOICES,
                              default=STATUS_CHOICES[0][0])
    is_block = models.BooleanField(verbose_name='заблокирована', default=False)

    customer = models.ManyToManyField(Customer, verbose_name='клиент')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец рассылки', default=1)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ['distribution_settings']

        permissions = [
            (
                'set_block',
                'Can block mailing'
            )
        ]


class Message(models.Model):
    title = models.CharField(max_length=100, verbose_name='тема')
    body = models.TextField(verbose_name='содержание', **NULLABLE)

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Log(models.Model):
    STATUS_CHOICES = [
        ('S', 'SUCCESSFUL'),
        ('UNS', 'UNSUCCESSFUL'),
    ]
    last_try = models.DateTimeField(verbose_name='время попытки', auto_now_add=True)
    status = models.CharField(verbose_name='статус попытки', choices=STATUS_CHOICES, max_length=20)
    response = models.TextField(verbose_name='ответ сервера')

    mailing_settings = models.ForeignKey(Mailing, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
