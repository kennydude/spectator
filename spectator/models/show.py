from django.db import models

from spectator.models import Channel


class Show(models.Model):
    """Represents a show. Commonly used by the storage
    backend
    """
    channel = models.ForeignKey(Channel)

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    cover = models.ImageField(null=True)
    genre = models.CharField(max_length=100, blank=True)
    show_type = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.name
