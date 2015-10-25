from rest_framework import serializers


class ItemSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    thumbnail = serializers.ImageField()


class ShowSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    cover = serializers.ImageField()


class ExtendedShowSerializer(ShowSerializer):
    items = ItemSerializer(many=True)
