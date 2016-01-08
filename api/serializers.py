from rest_framework import serializers

from .models import BucketList, Item


class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ('bucketlist', 'name', 'done')


class BucketListSerializer(serializers.ModelSerializer):
	item = ItemSerializer(many=True, read_only=True)

	class Meta:
		model = BucketList
		fields = ('name', 'item')
