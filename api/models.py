from django.db import models
from django.contrib.auth.models import User


class BucketList(models.Model):
	"""The Bucketlist model."""
	buck_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100, blank=False)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)

	@classmethod
	def create_bucketlist(cls, current_user, **kwargs):
		"""Create bucketlist method.

		Enforces the value of the "created_by" field to be the currently logged
		in user.
		"""

		bl = BucketList(
			name=kwargs.get('name'),
			created_by=current_user
		)
		bl.save()

	def __str__(self):
		"""Bucketlist's instance representation."""
		return self.name


class Item(models.Model):
	"""The Item model."""
	item_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100, blank=False)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	done = models.BooleanField(default=False)
	bucketlist = models.ForeignKey(
		BucketList,
		on_delete=models.CASCADE,
		related_name='item'
	)

	ef __str__(self):
		"""Item's instance representation."""
		return self.name