from .forms import MyForm


class NtbookSearchForm(forms.Form):
    ntbresult = forms.CharField(required=False, widget=forms.Textarea)

    form_class = MyForm
    # initial = {'key': 'value'}
    # template_name = 'form_template.html'
