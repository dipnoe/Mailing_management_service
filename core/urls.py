from django.urls import path
from django.views.decorators.cache import cache_page

from core.apps import CoreConfig
from core.views import contacts, home

app_name = CoreConfig.name

urlpatterns = [
    path('contacts/', cache_page(60)(contacts), name='contacts'),
    path('', home, name='home'),
]
