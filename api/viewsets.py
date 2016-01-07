from rest_framework import viewsets

from .serializers import BucketListSerializer, ItemSerializer
from .models import BucketList, Item


class BucketListViewSet(viewsets.ModelViewSet):

	serializer_class = BucketListSerializer
	queryset = BucketList.objects.all()


class ItemViewSet(viewsets.ModelViewSet):

	serializer_class = ItemSerializer
	queryset = Item.objects.all()
