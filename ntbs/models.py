from django.db import models

from django.core.urlresolvers import reverse

class Ntbook(models.Model):
    name = models.CharField(max_length=2048)
    meta = models.CharField(max_length=2048)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ntb_edit', kwargs={'pk': self.pk})
