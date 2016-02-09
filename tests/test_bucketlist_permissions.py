from .test_base import TestBaseClass

from api.models import BucketList


class TestBucketListPermissions(TestBaseClass):
	"""Create two users and test permissions on their respective bucketlists."""

	def test_get_bucketlist_other_user(self):
		"""Test get operation on bucketlist belonging to another user."""
		# create user 1
		self.create_user(self.user1)
		# login user 1
		response = self.client.post('/auth/login/', self.user1)
		token1 = 'JWT ' + response.data.get('token', None)
		# set authentication token in header
		self.client.credentials(HTTP_AUTHORIZATION=token1)
		# create bucketlist
		bucketlist1 = {
			'name': self.fake.name()
		}
		self.client.post('/bucketlists/', bucketlist1)
		# send get request to /bucketlists/ and then retrieve bucketlist id
		response = self.client.get('/bucketlists/')
		results_list = response.data.get('results')
		bucketlist1_id = results_list[0].get('buck_id')
		# remove user1 credentials from test client
		self.client.credentials()

		# create user 2
		self.create_user(self.user2)
		# login user 2
		response = self.client.post('/auth/login/', self.user2)
		token2 = 'JWT ' + response.data.get('token', None)
		# set authentication token in header
		self.client.credentials(HTTP_AUTHORIZATION=token2)
		# attempt get on user1's bucketlist
		response = self.client.get('/bucketlists/' + str(bucketlist1_id) + '/')

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.status_text, 'OK')
		self.assertEqual(response.data.get('name'), bucketlist1.get('name'))
		self.assertNotEqual(
			response.data.get('created_by'),
			self.user2.get('username')
		)

	def test_put_bucketlist_other_user(self):
		"""Test put operation on bucketlist belonging to another user."""
		# create user 1
		self.create_user(self.user1)
		# login user 1
		response = self.client.post('/auth/login/', self.user1)
		token1 = 'JWT ' + response.data.get('token', None)
		# set authentication token in header
		self.client.credentials(HTTP_AUTHORIZATION=token1)
		# create bucketlist
		bucketlist1 = {
			'name': self.fake.name()
		}
		self.client.post('/bucketlists/', bucketlist1)
		# send get request to /bucketlists/ and then retrieve bucketlist id
		response = self.client.get('/bucketlists/')
		results_list = response.data.get('results')
		bucketlist1_id = results_list[0].get('buck_id')
		# remove user1 credentials from test client
		self.client.credentials()

		# create user 2
		self.create_user(self.user2)
		# login user 2
		response = self.client.post('/auth/login/', self.user2)
		token2 = 'JWT ' + response.data.get('token', None)
		# set authentication token in header
		self.client.credentials(HTTP_AUTHORIZATION=token2)
		# attempt put on user1's bucketlist
		new_data = {
			'name': self.fake.name()
		}
		response = self.client.put(
			'/bucketlists/' + str(bucketlist1_id) + '/',
			new_data
		)
		self.assertEqual(response.status_code, 403)
		self.assertEqual(response.status_text, 'Forbidden')
		self.assertEqual(
			response.data.get('detail'),
			'You do not have permission to perform this action.'
		)

	def test_delete_bucketlist_other_user(self):
		"""Test delete operation on bucketlist belonging to another user."""
		# create user 1
		self.create_user(self.user1)
		# login user 1
		response = self.client.post('/auth/login/', self.user1)
		token1 = 'JWT ' + response.data.get('token', None)
		# set authentication token in header
		self.client.credentials(HTTP_AUTHORIZATION=token1)
		# create bucketlist
		bucketlist1 = {
			'name': self.fake.name()
		}
		self.client.post('/bucketlists/', bucketlist1)
		# send get request to /bucketlists/ and then retrieve bucketlist id
		response = self.client.get('/bucketlists/')
		results_list = response.data.get('results')
		bucketlist1_id = results_list[0].get('buck_id')
		# remove user1 credentials from test client
		self.client.credentials()

		# create user 2
		self.create_user(self.user2)
		# login user 2
		response = self.client.post('/auth/login/', self.user2)
		token2 = 'JWT ' + response.data.get('token', None)
		# set authentication token in header
		self.client.credentials(HTTP_AUTHORIZATION=token2)

		response = self.client.delete('/bucketlists/' + str(bucketlist1_id) + '/')
		self.assertEqual(response.status_code, 403)
		self.assertEqual(response.status_text, 'Forbidden')
		self.assertEqual(
			response.data.get('detail'),
			'You do not have permission to perform this action.'
		)