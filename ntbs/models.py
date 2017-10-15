from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class Ntbook(models.Model):
    snippet = models.TextField(max_length=2048)
    meta = models.TextField(max_length=2048, blank=True)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.snippet

    def get_absolute_url(self):
        return reverse('ntbook_edit', kwargs={'pk': self.pk})
