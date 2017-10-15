from django.db import models

from django.core.urlresolvers import reverse

class Ntbook(models.Model):
    name = models.TextField(max_length=2048)
    meta = models.TextField(max_length=2048, blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ntbook_edit', kwargs={'pk': self.pk})
