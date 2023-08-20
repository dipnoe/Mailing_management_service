from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogView, BlogDetailView

app_name = BlogConfig.name
urlpatterns = [
    path('', cache_page(60)(BlogView.as_view()), name='list_blog'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='detail_blog')
]
