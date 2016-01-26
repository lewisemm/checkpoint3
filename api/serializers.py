from rest_framework import serializers
from django.contrib.auth.models import User

from .models import BucketList, Item


class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ('item_id', 'name', 'date_created', 'date_modified', 'done')


class BucketListSerializer(serializers.ModelSerializer):
	item = ItemSerializer(many=True, read_only=True)

	class Meta:
		model = BucketList
		fields = (
			'buck_id', 'name', 'item', 'date_created',
			'date_modified', 'created_by'
		)


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'username')
