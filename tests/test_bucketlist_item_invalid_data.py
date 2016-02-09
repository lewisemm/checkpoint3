from random import random

from .test_base import TestBaseClass

from api.models import Item


class TestBucketListItemInvalidData(TestBaseClass):
	"""Test responses when invalid data is provided."""

	def random_done_status(self):
		"""Return a random status for the done field in bucketlist items."""
		done = [True, False]
		rand_index = int(2 * random())
		return done[rand_index]

	def test_post_invalid_bucketlist_item(self):
		"""Test response when a post with invalid bucketlist item details is sent."""
		# create user 1
		self.create_user(self.user1)
		# login user 1
		response = self.client.post('/auth/login/', self.user1)
		token = 'JWT ' + response.data.get('token', None)
		# set authentication token in header
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
		# post item under bucketlsit (missing name)
		new_item = {
			'name': '',
			'done': self.random_done_status()
		}
		response = self.client.post(
			'/bucketlists/' + str(bucketlist_id) + '/items/',
			new_item
		)
		self.assertTrue(
			'This field may not be blank.' in response.data.get('name')[0]
		)
		self.assertEqual(response.status_code, 400)
		self.assertEqual(response.status_text, 'Bad Request')

		# post item under bucketlsit (string as a done status)
		new_item1 = {
			'name': self.fake.name(),
			'done': 'some string'
		}
		response = self.client.post(
			'/bucketlists/' + str(bucketlist_id) + '/items/',
			new_item1
		)
		self.assertTrue(
			'is not a valid boolean.' in response.data.get('done')[0]
		)
		self.assertEqual(response.status_code, 400)
		self.assertEqual(response.status_text, 'Bad Request')

		# post item under bucketlsit (name and done have invalid data)
		new_item2 = {
			'name': '',
			'done': 'some string'
		}
		response = self.client.post(
			'/bucketlists/' + str(bucketlist_id) + '/items/',
			new_item2
		)
		self.assertTrue(
			' is not a valid boolean.' in response.data.get('done')[0]
		)
		self.assertTrue(
			'This field may not be blank' in response.data.get('name')[0]
		)
		self.assertEqual(response.status_code, 400)
		self.assertEqual(response.status_text, 'Bad Request')

	def test_put_invalid_bucketlist_item(self):
		"""Test response when a put with invalid bucketlist item details is sent."""
		# create user 1
		self.create_user(self.user1)
		# login user 1
		response = self.client.post('/auth/login/', self.user1)
		token = 'JWT ' + response.data.get('token', None)
		# set authentication token in header
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
		# create a bucketlist
		new_item = {
			'name': self.fake.name(),
			'done': self.random_done_status()
		}
		response = self.client.post(
			'/bucketlists/' + str(bucketlist_id) + '/items/',
			new_item
		)
		# get the item id
		response = self.client.get(
			'/bucketlists/' + str(bucketlist_id) + '/items/'
		)
		item_id = response.data[0].get('item_id')
		# send put request without name
		new_item1 = {
			'name': '',
			'done': self.random_done_status()
		}
		response = self.client.put(
			'/bucketlists/' + str(bucketlist_id) + '/items/' + str(item_id) + '/',
			new_item1
		)
		self.assertTrue(
			'This field may not be blank' in response.data.get('name')[0]
		)
		self.assertEqual(response.status_code, 400)
		self.assertEqual(response.status_text, 'Bad Request')

		# send put request with invalid boolean value
		new_item2 = {
			'name': self.fake.name(),
			'done': 'some string'
		}
		response = self.client.put(
			'/bucketlists/' + str(bucketlist_id) + '/items/' + str(item_id) + '/',
			new_item2
		)
		self.assertTrue(
			' is not a valid boolean.' in response.data.get('done')[0]
		)
		self.assertEqual(response.status_code, 400)
		self.assertEqual(response.status_text, 'Bad Request')

		# send put request with invalid bucketlist item values
		new_item2 = {
			'name': '',
			'done': 'some string'
		}
		response = self.client.put(
			'/bucketlists/' + str(bucketlist_id) + '/items/' + str(item_id) + '/',
			new_item2
		)
		self.assertTrue(
			' is not a valid boolean.' in response.data.get('done')[0]
		)
		self.assertTrue(
			'This field may not be blank' in response.data.get('name')[0]
		)
		self.assertEqual(response.status_code, 400)
		self.assertEqual(response.status_text, 'Bad Request')