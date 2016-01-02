from test_base_class import TestBaseClass

class TestBucketList(TestBaseClass):

	def test_create_bucketlist(self):
		"""
		Tests successful creation of a bucketlist.
		"""
		# create a user
		self.create_user()
		# log them in
		self.client.post('/auth/login')