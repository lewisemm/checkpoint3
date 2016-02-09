from random import random

from .test_base import TestBaseClass

from api.models import Item


class TestBucketListItems(TestBaseClass):
	"""Test all permissible http methods on bucketlist items."""

	def random_done_status(self):
		"""Return a random status for the done field in bucketlist items."""
		done = [True, False]
		rand_index = int(2 * random())
		return done[rand_index]

	def test_successful_get_bucketlist_item(self):
		"""Test successful get operation on existing bucketlist item."""
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
		# post item under bucketlsit
		new_item = {
			'name': self.fake.name(),
			'done': self.random_done_status()
		}
		self.client.post(
			'/bucketlists/' + str(bucketlist_id) + '/items/',
			new_item
		)
		# get the item's id
		response = self.client.get(
			'/bucketlists/' + str(bucketlist_id) + '/items/'
		)
		self.assertEqual(response.data[0].get('name'), new_item.get('name'))
		self.assertEqual(response.status_text, 'OK')
		self.assertEqual(response.status_code, 200)
		# check the item's bucketlist relationship from the DB
		item_id = response.data[0].get('item_id')
		item_obj = Item.objects.get(item_id=item_id)
		self.assertEqual(item_obj.bucketlist.name, bucketlist.get('name'))

	def test_successful_post_bucketlist_item(self):
		"""Test successful get operation on existing bucketlist item."""
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
		# post item under bucketlsit
		new_item = {
			'name': self.fake.name(),
			'done':	self.random_done_status()
		}
		self.client.post(
			'/bucketlists/' + str(bucketlist_id) + '/items/',
			new_item
		)
		# get the new item in bucketlist
		response = self.client.get(
			'/bucketlists/' + str(bucketlist_id) + '/items/'
		)
		self.assertEqual(response.data[0].get('name'), new_item.get('name'))
		self.assertEqual(response.status_text, 'OK')
		self.assertEqual(response.status_code, 200)
		# check the item's bucketlist relationship from the DB
		item_id = response.data[0].get('item_id')
		item_obj = Item.objects.get(item_id=item_id)
		self.assertEqual(item_obj.bucketlist.name, bucketlist.get('name'))

	def test_successful_put_bucketlist_item(self):
		"""Test successful put operation on existing bucketlist item."""
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
		# post item under bucketlsit
		new_item = {
			'name': self.fake.name(),
			'done': self.random_done_status()
		}
		self.client.post(
			'/bucketlists/' + str(bucketlist_id) + '/items/',
			new_item
		)
		# get the item's id
		response = self.client.get(
			'/bucketlists/' + str(bucketlist_id) + '/items/'
		)
		item_id = response.data[0].get('item_id')
		# attempt a put request
		new_item_data = {
			'name': self.fake.name(),
			'done': self.random_done_status()
		}
		self.client.put(
			'/bucketlists/' + str(bucketlist_id) + '/items/' + str(item_id) + '/',
			new_item_data
		)
		# send a get and check assertions
		response = self.client.get(
			'/bucketlists/' + str(bucketlist_id) + '/items/' + str(item_id) + '/',
		)
		self.assertEqual(response.data.get('name'), new_item_data.get('name'))
		self.assertEqual(response.data.get('done'), new_item_data.get('done'))
		self.assertNotEqual(response.data.get('name'), new_item.get('name'))
		self.assertEqual(response.status_text, 'OK')
		self.assertEqual(response.status_code, 200)

	def test_successful_delete_bucketlist_item(self):
		"""Test successful delete operation on existing bucketlist item."""
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
		# post item under bucketlsit
		new_item = {
			'name': self.fake.name(),
			'done': self.random_done_status()
		}
		self.client.post(
			'/bucketlists/' + str(bucketlist_id) + '/items/',
			new_item
		)
		# get the item's id
		response = self.client.get(
			'/bucketlists/' + str(bucketlist_id) + '/items/'
		)
		item_id = response.data[0].get('item_id')
		# attempt a delete request
		response = self.client.delete(
			'/bucketlists/' + str(bucketlist_id) + '/items/' + str(item_id) + '/'
		)
		self.assertEqual(response.status_code, 204)
		self.assertEqual(response.status_text, 'No Content')
		# confirm 404 response with get request after delete
		response = self.client.get(
			'/bucketlists/' + str(bucketlist_id) + '/items/' + str(item_id) + '/'
		)
		self.assertEqual(response.status_code, 404)
		self.assertEqual(response.status_text, 'Not Found')
		self.assertEqual(response.data.get('detail'), 'Not found.')

	def test_unauthenticated_get_bucketlist_item(self):
		"""Test unauthenticated get operation on existing bucketlist item."""
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
		# post item under bucketlist
		new_item = {
			'name': self.fake.name(),
			'done': self.random_done_status()
		}
		self.client.post(
			'/bucketlists/' + str(bucketlist_id) + '/items/',
			new_item
		)
		# get the item's id
		response = self.client.get(
			'/bucketlists/' + str(bucketlist_id) + '/items/'
		)
		item_id = response.data[0].get('item_id')
		# remove authorization credentials from test client
		self.client.credentials()
		# test get item without credentials
		response = self.client.get(
			'/bucketlists/' + str(bucketlist_id) + '/items/' + str(item_id) + '/'
		)
		self.assertEqual(response.data.get('name'), new_item.get('name'))
		self.assertEqual(response.status_text, 'OK')
		self.assertEqual(response.status_code, 200)

	def test_unauthenticated_put_bucketlist_item(self):
		"""Test unauthenticated put operation on existing bucketlist item."""
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
		# post item under bucketlist
		new_item = {
			'name': self.fake.name(),
			'done': self.random_done_status()
		}
		self.client.post(
			'/bucketlists/' + str(bucketlist_id) + '/items/',
			new_item
		)
		# get the item's id
		response = self.client.get(
			'/bucketlists/' + str(bucketlist_id) + '/items/'
		)
		item_id = response.data[0].get('item_id')
		# remove authorization credentials from test client
		self.client.credentials()
		# test put on bucketlist item without credentials
		new_item_data = {
			'name': self.fake.name(),
			'done': self.random_done_status()
		}
		response = self.client.put(
			'/bucketlists/' + str(bucketlist_id) + '/items/' + str(item_id) + '/',
			new_item_data
		)
		self.assertEqual(
			response.data.get('detail'),
			'Authentication credentials were not provided.'
		)
		self.assertEqual(response.status_text, 'Unauthorized')
		self.assertEqual(response.status_code, 401)

	def test_unauthenticated_post_bucketlist_item(self):
		"""Test unauthenticated post operation on existing bucketlist item."""
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
		# remove authentication credentials
		self.client.credentials()
		# post item under bucketlist without authorization token
		new_item = {
			'name': self.fake.name(),
			'done': self.random_done_status()
		}
		response = self.client.post(
			'/bucketlists/' + str(bucketlist_id) + '/items/',
			new_item
		)
		self.assertEqual(
			response.data.get('detail'),
			'Authentication credentials were not provided.'
		)
		self.assertEqual(response.status_text, 'Unauthorized')
		self.assertEqual(response.status_code, 401)

	def test_unauthenticated_delete_bucketlist_item(self):
		"""Test unauthenticated delete operation on existing bucketlist item."""
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
		# post item under bucketlist
		new_item = {
			'name': self.fake.name(),
			'done': self.random_done_status()
		}
		self.client.post(
			'/bucketlists/' + str(bucketlist_id) + '/items/',
			new_item
		)
		# get the item's id
		response = self.client.get(
			'/bucketlists/' + str(bucketlist_id) + '/items/'
		)
		item_id = response.data[0].get('item_id')
		# remove authorization credentials from test client
		self.client.credentials()
		# test delete
		response = self.client.delete(
			'/bucketlists/' + str(bucketlist_id) + '/items/' + str(item_id) + '/'
		)
		self.assertEqual(
			response.data.get('detail'),
			'Authentication credentials were not provided.'
		)
		self.assertEqual(response.status_text, 'Unauthorized')
		self.assertEqual(response.status_code, 401)