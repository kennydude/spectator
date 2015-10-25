from django.db import models


class Channel(models.Model):
    '''A channel represents something which can provide content
    '''
    name = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)
    configuration = models.TextField()

    def __unicode__(self):
        return self.name
