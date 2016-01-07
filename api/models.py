from django.db import models


class BucketList(models.Model):
	buck_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100, blank=False)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	created_by = models.CharField(
		max_length=100,
		blank=False,
		default='Unauthenticated'
	)

	@classmethod
	def create_bucketlist(cls, current_user, **kwargs):
		"""Create bucketlist method.

		Enforces the value of the "created_by" field to be the currently logged
		in user.
		"""

		bl = BucketList(
			name=kwargs.get('name'),
			created_by=current_user.username
		)
		bl.save()


class Item(models.Model):
	item_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100, blank=False)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	done = models.BooleanField(default=False)
	bucketlist = models.ForeignKey(BucketList, on_delete=models.CASCADE)
