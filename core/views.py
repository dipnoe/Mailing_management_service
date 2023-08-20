from django.shortcuts import render
from django.views.generic import TemplateView

from blog.models import Blog
from mailing.models import Message, Mailing, Customer


# Create your views here.
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Новый контакт!\n{name} ({email}) написал: {message}\n')
    return render(request, 'core/contacts.html')


def home(request):
    mailing_count = Mailing.objects.all()
    active_mailing_count = Mailing.objects.filter(status='CR')
    unique_clients = Customer.objects.all()
    blog = Blog.objects.all()[:3]

    context = {
        'mailing_count': mailing_count,
        'active_mailing_count': active_mailing_count,
        'unique_clients': unique_clients,
        'blog': blog
    }
    return render(request, 'core/home.html', context)
