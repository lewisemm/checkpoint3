from .test_base import TestBaseClass

from api.models import BucketList


class TestBucketListInvalidData(TestBaseClass):
	"""Test responses when invalid data is submitted."""

	def test_post_invalid_bucketlist_name(self):
		"""Test response when invalid data is submitted on '/bucketlist/' url."""
		# create user
		self.create_user(self.user1)
		# login user
		response = self.client.post('/auth/login/', self.user1)
		token = 'JWT ' + response.data.get('token', None)
		# set authentication token in headre
		self.client.credentials(HTTP_AUTHORIZATION=token)
		# create bucketlist
		bucketlist = {
			'name': ''
		}
		response = self.client.post('/bucketlists/', bucketlist)
		self.assertEqual(response.data.get('name')[0], 'This field may not be blank.')
		self.assertEqual(response.status_code, 400)
		self.assertEqual(response.status_text, 'Bad Request')

	def test_put_invalid_bucketlist_name(self):
		"""Test response when invalid data is submitted on '/bucketlist/buck_id' url."""
		# create user
		self.create_user(self.user1)
		# login user
		response = self.client.post('/auth/login/', self.user1)
		token = 'JWT ' + response.data.get('token', None)
		# set authentication token in headre
		self.client.credentials(HTTP_AUTHORIZATION=token)
		# create bucketlist
		bucketlist = {
			'name': self.fake.name()
		}
		self.client.post('/bucketlists/', bucketlist)
		# send get request to /bucketlists/ and then retrieve bucketlist id
		response = self.client.get('/bucketlists/')
		results_list = response.data.get('results')
		bucketlist_id = results_list[0].get('buck_id')
		# append id of bucketlist just created in the url and edit it
		new_data = {
			'name': ''
		}
		response = self.client.put(
			'/bucketlists/' + str(bucketlist_id) + '/',
			new_data
		)
		self.assertEqual(response.data.get('name')[0], 'This field may not be blank.')
		self.assertEqual(response.status_code, 400)
		self.assertEqual(response.status_text, 'Bad Request')