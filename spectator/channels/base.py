class BaseChannel(object):
    '''A channel represents how spectator gets content.

    This is a base version which doesn't do anything. See the examples
    and documentation for more information :)
    '''

    def __init__(self, channel):
        '''Setup the channel based on the channel object provided
        '''
        pass

    def get_shows(self):
        '''Returns the shows contained on this channel. You should return a
        QuerySet or similar to reduce overheads
        '''
        raise NotImplementedError("Channel.get_shows() not implemented")

    def get_show(self, show_id):
        '''Returns the specified show ID. You should return a list of items
        as well
        '''
        raise NotImplementedError("Channel.get_show(show_id) not implemented")

    def get_item(self, item_id):
        '''Returns the specified show ID
        '''
        raise NotImplementedError("Channel.get_item(item_id) not implemented")

    def get_item_stream(self, item_id):
        '''Gets the show's stream. If the stream is remote, now is the
        time to run anything to get it!
        '''
        raise NotImplementedError("Channel.get_item_stream(item_id) not implemented")

    def get_icon(self):
        '''Returns a filename from the static directory containing
        an icon to use for your source. SVG is reconmended
        '''
        raise NotImplementedError("Channel.get_icon() not implemented")
