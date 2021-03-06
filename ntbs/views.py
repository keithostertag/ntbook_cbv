from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
# from django import forms
from django.forms import ModelForm, Textarea

from ntbs.models import Ntbook

class NtbookForm(ModelForm):    # using this form for create and update
    class Meta:
        model = Ntbook
        fields = ('snippet', 'meta')
        # customize because the default is too small visually
        widgets = {
            'snippet': Textarea(attrs={'class': 'form_snippet'}),
            'meta': Textarea(attrs={'class': 'form_meta'}),
        }

class NtbookList(ListView):
    model = Ntbook

# pass total_snippets to the ListView so we can display it
    def get_context_data(self, **kwargs):
            context = super(NtbookList, self).get_context_data(**kwargs)
            context['total_snippets'] = Ntbook.objects.filter().count()
            return context

# We search both the snippet and meta fields for strings/keywords.
# Using icontains is adequate for this type/size application.
# order_by('-created_at') will give us the list in reverse chrono order

    def get_queryset(self):
        try:
            q = (Ntbook.objects.order_by('-created_at').filter(meta__icontains=self.request.GET['q'])
                | Ntbook.objects.order_by('-created_at').filter(snippet__icontains=self.request.GET['q']))
            return q
        except:
            return Ntbook.objects.order_by('-created_at').all()

# In the following, we need to include the fields for creating and updating.
# Use reverse_lazy to return to the main template ntbook_list.html after completing each generic view.
class NtbookCreate(CreateView):
    model = Ntbook
    success_url = reverse_lazy('ntbook_list')
    form_class = NtbookForm # customize form using NtbookForm

class NtbookUpdate(UpdateView):
    model = Ntbook
    success_url = reverse_lazy('ntbook_list')
    form_class = NtbookForm # customize form using NtbookForm

class NtbookDelete(DeleteView):
    model = Ntbook
    success_url = reverse_lazy('ntbook_list')
