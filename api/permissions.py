from rest_framework import permissions
from .models import BucketList


class IsOwnerOrReadOnly(permissions.BasePermission):
	"""Custom permission to restrict unsafe methods to owners."""

	def has_object_permission(self, request, view, obj):
		"""Allow GET, HEAD and OPTIONS requests from anyone."""
		if request.method in permissions.SAFE_METHODS:
			return True

		if isinstance(obj, BucketList):
			return obj.created_by == request.user.username

		return obj.bucketlist.created_by == request.user.username
