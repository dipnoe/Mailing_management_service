from django.contrib import admin

from mailing.models import Message, Customer, Mailing, Log


# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
    list_filter = ('title',)


@admin.register(Mailing)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = ('distribution_settings', 'frequency', 'status',)


@admin.register(Customer)
class Customer(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email',)


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('last_try', 'status', 'response',)
