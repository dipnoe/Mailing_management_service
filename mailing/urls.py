from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import (MailingListView, MailingCreateView, MailingUpdateView, MailingDeleteView,
                           CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDetailView,
                           CustomerDeleteView, hide_mailing, MessageDetail, LogView)

app_name = MailingConfig.name

urlpatterns = [
    path('mailing/', MailingListView.as_view(), name='list_mailing'),
    path('hide_mailing/', hide_mailing, name='hide_mailing'),
    path('mailing/create/', MailingCreateView.as_view(), name='create_mailing'),
    path('mailing/detail/<int:pk>', MessageDetail.as_view(), name='detail_message'),
    path('mailing/update/<int:pk>', MailingUpdateView.as_view(), name='update_mailing'),
    path('mailing/delete/<int:pk>', MailingDeleteView.as_view(), name='delete_mailing'),
    path('mailing/log', LogView.as_view(), name='list_log'),

    path('customer/', CustomerListView.as_view(), name='list_customer'),
    path('customer/detail/<int:pk>', CustomerDetailView.as_view(), name='detail_customer'),
    path('customer/create/', CustomerCreateView.as_view(), name='create_customer'),
    path('customer/update/<int:pk>', CustomerUpdateView.as_view(), name='update_customer'),
    path('customer/delete/<int:pk>', CustomerDeleteView.as_view(), name='delete_customer'),
]
