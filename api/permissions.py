from rest_framework import permissions
from .models import BucketList


class IsOwner(permissions.BasePermission):
	"""Custom permission to restrict unsafe methods to owners."""

	def has_object_permission(self, request, view, obj):
		"""Grant full access only when the request is from the bucketlist creator."""

		if isinstance(obj, BucketList):
			return obj.created_by == request.user
