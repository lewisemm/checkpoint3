from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import BucketListSerializer, ItemSerializer
from .models import BucketList, Item


class BucketListViewSet(viewsets.ModelViewSet):

	serializer_class = BucketListSerializer
	queryset = BucketList.objects.all()

	def create(self, request):
		"""Customize the BucketList creation process.

		Save the currently logged in user as the creator of the
		bucketlist.
		"""
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			current_user = request.user
			BucketList.create_bucketlist(current_user, **serializer.validated_data)
			return Response(
				{
					'status': 'Success',
					'message': 'BucketList created'
				},
				status=status.HTTP_201_CREATED
			)
		return Response(
			{
				'status': "Bad request",
				'message': "Failed to create an BucketList"
			},
			status=status.HTTP_401_BAD_REQUEST
		)


class ItemViewSet(viewsets.ModelViewSet):

	serializer_class = ItemSerializer
	queryset = Item.objects.all()
