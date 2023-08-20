import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from mailing.forms import MessageForm, MailingForm, CustomerForm
from mailing.models import Message, Mailing, Customer, Log
from mailing.services import send_mailing


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(owner=self.request.user.pk)
        return queryset


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:list_mailing')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        MessageFormset = inlineformset_factory(Mailing, Message, form=MessageForm)
        if self.request.method == 'POST':
            context_data['formset'] = MessageFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = MessageFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        send_mailing(message=Message(mailing_id=self.object.id), mailing=self.object)
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:list_mailing')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MessageFormset = inlineformset_factory(Mailing, Message, form=MessageForm)
        if self.request.method == 'POST':
            context_data['formset'] = MessageFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = MessageFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:list_mailing')


class MessageDetail(DetailView):
    model = Message


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    form_class = CustomerForm
    permission_required = ''


class CustomerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Customer
    fields = ('email', 'last_name', 'first_name')
    success_url = reverse_lazy('mailing:list_customer')
    permission_required = 'mailing.add_customer'


class CustomerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Customer
    fields = ('email', 'last_name', 'first_name')
    success_url = reverse_lazy('mailing:list_customer')
    permission_required = 'mailing.change_customer'


class CustomerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('mailing:list_customer')
    permission_required = 'mailing.delete_customer'


def hide_mailing(request):
    if 'mailing_id' in request.GET:
        mailing_id = request.GET.get('mailing_id')
        mailing = Mailing.objects.get(id=mailing_id)
        mailing.save()
        mailing.is_block = True
        mailing.save()
        return redirect('mailing:list_mailing')

    mailings = Mailing.objects.all()
    context = {'mailing': mailings}
    return render(request, 'mailing:mailing_list.html', context)


class LogView(LoginRequiredMixin, ListView):
    model = Log
