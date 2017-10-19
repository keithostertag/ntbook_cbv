from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from ntbs.models import Ntbook

class NtbookList(ListView):
    model = Ntbook


# In the following, we need to include the fields for creating and updating
# Use reverse_lazy to return to the main template ntbook_list.html after completing each generic view
class NtbookCreate(CreateView):
    model = Ntbook
    success_url = reverse_lazy('ntbook_list')
    fields = ['snippet', 'meta']

class NtbookUpdate(UpdateView):
    model = Ntbook
    success_url = reverse_lazy('ntbook_list')
    fields = ['snippet', 'meta']

class NtbookDelete(DeleteView):
    model = Ntbook
    success_url = reverse_lazy('ntbook_list')
