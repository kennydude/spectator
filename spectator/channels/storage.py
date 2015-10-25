import os
import mimetypes

from spectator.channels import BaseChannel
from spectator.models import Show, Item


class StorageChannel(BaseChannel):
    '''Channel based on storage on the local disk and database
    '''
    def __init__(self, channel):
        self.channel = channel

    def get_shows(self):
        return Show.objects.filter(channel=self.channel)

    def get_show(self, show_id):
        return Show.objects.get(id=show_id,
            channel=self.channel)

    def get_item(self, item_id):
        return Item.objects.get(id=item_id, show__channel=self.channel)

    def get_item_stream(self, item_id):
        it = self.get_item(item_id)
        return (
            open(it.source, 'rb'),
            mimetypes.guess_type(it.source)[0],
            os.path.getsize(it.source)
        )
