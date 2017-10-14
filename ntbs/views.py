from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from ntbs.models import Ntbook

class NtbookList(ListView):
    model = Ntbook

class NtbookCreate(CreateView):
    model = Ntbook
    success_url = reverse_lazy('ntb_list')
    fields = ['name', 'meta']

class NtbookUpdate(UpdateView):
    model = Ntbook
    success_url = reverse_lazy('ntb_list')
    fields = ['name', 'meta']

class NtbookDelete(DeleteView):
    model = Ntbook
    success_url = reverse_lazy('ntb_list')
