from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
# from django.forms import ModelForm, modelformset_factory
# from django.http import HttpResponseRedirect
from django import forms

from ntbs.models import Ntbook

class NtbookList(ListView):
    model = Ntbook

# We search both the snippet and meta fields for strings/keywords.
# Using icontains is adequate for this type/size application.
    def get_queryset(self):
            try:
                q = (Ntbook.objects.filter(meta__icontains=self.request.GET['q'])
                    | Ntbook.objects.filter(snippet__icontains=self.request.GET['q']))
                return q
            except:
                return Ntbook.objects.all()

# In the following, we need to include the fields for creating and updating.
# Use reverse_lazy to return to the main template ntbook_list.html after completing each generic view.
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
