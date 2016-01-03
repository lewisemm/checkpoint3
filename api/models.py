from django.db import models

class BucketList(models.Model):
	buck_id = models.CharField(max_length=10, primary_key=True)
	name = models.CharField(max_length=100)
	date_created = models.DateField(auto_now_add=True)
	date_modified = models.DateField(auto_now=True)
	created_by = models.CharField(max_length=100)

class Item(models.Model):
	item_id = models.CharField(max_length=10, primary_key=True)
	name = models.CharField(max_length=100)
	date_created = models.DateField(auto_now_add=True)
	date_modified = models.DateField(auto_now=True)
	done = models.BooleanField(default=False)
	bucketlist = models.ForeignKey(BucketList, on_delete=models.CASCADE)