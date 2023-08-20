from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogView, BlogDetailView

app_name = BlogConfig.name
urlpatterns = [
    path('', BlogView.as_view(), name='list_blog'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='detail_blog')
]
