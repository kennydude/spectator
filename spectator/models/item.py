from django.db import models

from spectator.models import Show


class Item(models.Model):
    """Item in the database. Typical an episode, but "shows"
    can be movies etc
    """
    show = models.ForeignKey(Show, related_name='items')

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(null=True)
    source = models.TextField()

    def __unicode__(self):
        return "{} from {}".format(self.name, self.show)
