from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from rest_framework import status, viewsets, permissions
from rest_framework.response import Response

from .serializers import BucketListSerializer, ItemSerializer, UserSerializer
from .models import BucketList, Item
from .permissions import IsOwner
from .paginator import BucketlistPaginator


class BucketListViewSet(viewsets.ModelViewSet):
	"""Handle CRUD requests to '/bucketlists/' url."""
	queryset = BucketList.objects.all()
	serializer_class = BucketListSerializer
	permission_classes = (
		permissions.IsAuthenticated,
		IsOwner,
	)
	pagination_class = BucketlistPaginator

	def get_queryset(self):
		# permissions will handle cases where bucketlist doesn't belong to
		# current user
		if self.kwargs.get('pk'):
			return BucketList.objects.filter(pk=self.kwargs.get('pk'))

		# restrict bucketlists to those of current user
		current_user = self.request.user.username
		search_name = self.request.query_params.get('q')
		if search_name:
			return BucketList.objects.filter(
				name__icontains=search_name,
				created_by=current_user
			)
		return BucketList.objects.filter(created_by=current_user)

	def get_object(self):
		obj = get_object_or_404(self.get_queryset())
		self.check_object_permissions(self.request, obj)
		return obj

	def create(self, request):
		"""Create bucketlist and save currently logged in user's username in the
		'created_by' field.
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
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemViewSet(viewsets.ModelViewSet):
	"""Handle CRUD requests to the '/bucketlists/<pk>/items/' url.
	"""
	serializer_class = ItemSerializer
	queryset = Item.objects.all()
	permission_classes = (
		permissions.IsAuthenticated,
	)

	def create(self, request, bucketlist_pk=None, pk=None):
		"""Create a bucketlist item in bucketlist of id 'bucketlist_pk'."""
		try:
			bucketlist = BucketList.objects.get(pk=bucketlist_pk)
			if bucketlist.created_by == request.user.username:
				serializer = self.serializer_class(data=request.data)
				if serializer.is_valid():
					item = Item(**serializer.validated_data)
					item.bucketlist = bucketlist
					item.save()
					return Response(
						{
							'status': 'Success',
							'message': 'BucketList item created'
						},
						status=status.HTTP_201_CREATED
					)
				return Response(
					serializer.errors,
					status=status.HTTP_400_BAD_REQUEST
				)
			return Response(
				{
					'detail': 'You do not have permission to perform this action.'
				}, status=status.HTTP_403_FORBIDDEN
			)
		except BucketList.DoesNotExist:
			return Response(
				{
					'detail': 'Not found.'
				}, status=status.HTTP_404_NOT_FOUND
			)

	def list(self, request, bucketlist_pk=None):
		"""Retrieve all bucketlist items in the bucketlist of id 'bucketlist_pk'."""
		try:
			bucketlist = BucketList.objects.get(buck_id=bucketlist_pk)
			if bucketlist.created_by == request.user.username:
				queryset = Item.objects.filter(bucketlist=bucketlist)
				serializer = ItemSerializer(queryset, many=True)
				return Response(serializer.data, status=status.HTTP_200_OK)
			return Response(
				{
					'detail': 'You do not have permission to perform this action.'
				}, status=status.HTTP_403_FORBIDDEN
			)
		except BucketList.DoesNotExist:
			return Response(
				{
					'detail': 'Not found.'
				}, status=status.HTTP_404_NOT_FOUND
			)

	def retrieve(self, request, pk=None, bucketlist_pk=None):
		"""Retrieve bucketlist item of id 'pk' in bucketlist of id 'bucketlist_pk'.
		"""
		try:
			bucketlist = BucketList.objects.get(
				buck_id=bucketlist_pk,
				created_by=request.user.username
			)
			queryset = Item.objects.filter(bucketlist=bucketlist, item_id=pk)
			item = get_object_or_404(queryset)
			serializer = ItemSerializer(item)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except BucketList.DoesNotExist:
			return Response(
				{
					'detail': 'You do not have permission to perform this action.'
				}, status=status.HTTP_403_FORBIDDEN
			)

	def destroy(self, request, pk=None, bucketlist_pk=None):
		"""Delete bucketlist item of id 'pk' in bucketlist of id 'bucketlist_pk'.
		"""
		bucketlist = BucketList.objects.get(buck_id=bucketlist_pk)
		if bucketlist.created_by == request.user.username:
			queryset = Item.objects.filter(bucketlist=bucketlist, item_id=pk)
			item = get_object_or_404(queryset)
			item.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		return Response(
			{
				'detail': 'You do not have permission to perform this action.'
			}, status=status.HTTP_403_FORBIDDEN
		)

	def update(self, request, pk=None, bucketlist_pk=None):
		"""Update bucketlist item of id 'pk' in bucketlist of id 'bucketlist_pk'.
		"""
		bucketlist = BucketList.objects.get(buck_id=bucketlist_pk)
		if bucketlist.created_by == request.user.username:
			queryset = Item.objects.filter(bucketlist=bucketlist, item_id=pk)
			item = get_object_or_404(queryset)
			serializer = self.serializer_class(data=request.data)
			if serializer.is_valid():
				item.name = serializer.validated_data.get('name')
				item.done = serializer.validated_data.get('done')
				item.save()
				return Response(
					serializer.data, status=status.HTTP_200_OK
				)
			return Response(
				serializer.errors, status=status.HTTP_400_BAD_REQUEST
			)
		return Response(
			{
				'detail': 'You do not have permission to perform this action.'
			}, status=status.HTTP_403_FORBIDDEN
		)


class UserViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()

	def create(self, request):
		"""Create new users."""
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			new_user = User.objects.create_user(**serializer.validated_data)
			new_user.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
