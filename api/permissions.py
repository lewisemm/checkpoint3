from rest_framework import permissions
from .models import BucketList


class IsOwnerOrReadOnly(permissions.BasePermission):
	"""Custom permission to restrict unsafe methods to owners."""

	def has_object_permission(self, request, view, obj):
		"""Allow GET, HEAD and OPTIONS requests from anyone."""
		if request.method in permissions.SAFE_METHODS:
			return True

		# if object is instance of BucketList, ensure unsafe methods can
		# only be requested by the owner
		if isinstance(obj, BucketList):
			return obj.created_by == request.user.username
		else:
			# this is an instance of Item
			# unsafe requests should only be granted for Items belonging
			# to BucketLists created by currently logged in user
			return obj.bucketlist.created_by == request.user.username
