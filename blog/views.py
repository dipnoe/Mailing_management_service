from django.core.cache import cache
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Blog
from config.settings import CACHE_ENABLED


# Create your views here.
class BlogView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def cache(self):
        if CACHE_ENABLED:
            key = f'blog_list_{self.object.pk}'
            blog_list = cache.get(key)
            if blog_list is None:
                blog_list = Blog.objects.all()
                cache.set(key, blog_list)
                return blog_list
        return Blog.objects.all()


    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
