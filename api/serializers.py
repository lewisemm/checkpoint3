from rest_framework import serializers

from .models import BucketList, Item


class BucketListSerializer(serializers.ModelSerializer):
	class Meta:
		model = BucketList
		fields = ('name',)


class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ('bucketlist', 'name', 'done')
