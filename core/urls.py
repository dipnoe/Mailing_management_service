from django.urls import path

from core.apps import CoreConfig
from core.views import contacts, home

app_name = CoreConfig.name

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', home, name='home'),
]
