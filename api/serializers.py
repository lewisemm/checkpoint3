from rest_framework import serializers
from django.contrib.auth.models import User

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


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'username')
