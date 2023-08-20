from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=50, verbose_name='почта', unique=True)
    phone = models.PositiveIntegerField(verbose_name='телефон', unique=True, **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    is_active = models.BooleanField(verbose_name='активный', default=True)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        permissions = [
            (
                'set_active',
                'Can deactivate user'
            )
        ]

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
