import datetime
import time

from django import forms
from django.core.exceptions import ValidationError

from mailing.models import Message, Mailing, Customer


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = ('title', 'body',)


class MailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ('distribution_settings', 'frequency',)

    # def clean_distribution_settings(self):
    #     cleaned_data = self.cleaned_data.get('distribution_settings')
    #
    #     # if cleaned_data.strftime() not in ('%H:%M:%S', '%H:%M'):
    #     if datetime.datetime.strptime(str(cleaned_data), '%H:%M'):
    #         raise forms.ValidationError('Ошибка формата времени.')
    #
    #     return cleaned_data


class CustomerForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
