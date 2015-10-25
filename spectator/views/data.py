from django.utils.module_loading import import_string

from rest_framework import viewsets

from spectator.models import Channel
from spectator.serializers import (ShowSerializer, ExtendedShowSerializer,
    ItemSerializer)


class BaseView(viewsets.ModelViewSet):
    def get_channel(self):
        obj = Channel.objects.get(id=self.kwargs['channel'])
        channel = import_string(obj.provider)(obj)
        return channel


class ListShowViewSet(BaseView):
    serializer_class = ShowSerializer

    def get_queryset(self):
        return self.get_channel().get_shows()


class ShowViewSet(BaseView):
    serializer_class = ExtendedShowSerializer

    def get_object(self):
        return self.get_channel().get_show(self.kwargs['pk'])


class ItemViewSet(BaseView):
    serializer_class = ItemSerializer

    def get_object(self):
        return self.get_channel().get_item(self.kwargs['pk'])
