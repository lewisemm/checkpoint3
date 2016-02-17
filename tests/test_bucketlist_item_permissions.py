from random import random

from .test_base import TestBaseClass

from api.models import Item


class TestBucketListItemPermissions(TestBaseClass):
	"""Test read/write permissions between the bucketlist creator and a second
	user.
	"""

	def random_done_status(self):
		"""Return a random status for the done field in bucketlist items."""
		done = [True, False]
		rand_index = int(2 * random())
		return done[rand_index]

	def test_get_bucketlist_item_other_user(self):
		"""Test get operation on '/bucketlists/<buck_id>/items/<item_id>' url when
		bucketlist has been created by a different user.
		"""
		# create user 1
		self.create_user(self.user1)
		# login user 1
		response = self.client.post('/auth/login/', self.user1)
		token1 = 'JWT ' + response.data.get('token', None)
		# set authentication token in header
		self.client.credentials(HTTP_AUTHORIZATION=token1)
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
		# get the id of the new item in bucketlist
		response = self.client.get(
			'/bucketlists/' + str(bucketlist_id) + '/items/'
		)
		item_id = response.data[0].get('item_id')
		# remove user1 credentials
		self.client.credentials()

		# create user 2
		self.create_user(self.user2)
		# login user 2
		response = self.client.post('/auth/login/', self.user2)
		token2 = 'JWT ' + response.data.get('token', None)
		# set authentication token in header
		self.client.credentials(HTTP_AUTHORIZATION=token2)
		# test get while authenticated as user2
		response = self.client.get(
			'/bucketlists/' + str(bucketlist_id) + '/items/' + str(item_id) + '/'
		)
		self.assertTrue(
			'You do not have permission to perform this action' in
			response.data.get('detail')
		)
		self.assertEqual(response.status_text, 'Forbidden')
		self.assertEqual(response.status_code, 403)

	def test_get_bucketlist_items_other_user(self):
		"""Test get operation on '/bucketlists/<buck_id>/items/' url when bucketlist
		has  been created by a different user.
		"""
		# create user 1
		self.create_user(self.user1)
		# login user 1
		response = self.client.post('/auth/login/', self.user1)
		token1 = 'JWT ' + response.data.get('token', None)
		# set authentication token in header
		self.client.credentials(HTTP_AUTHORIZATION=token1)
		# create bucketlist as user1
		bucketlist = {
			'name': self.fake.name()
		}
		self.client.post('/bucketlists/', bucketlist)
		# send get request to /bucketlists/ to retrieve bucketlist id
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
		# remove user1 credentials
		self.client.credentials()
		# create user 2
		self.create_user(self.user2)
		# login user 2
		response = self.client.post('/auth/login/', self.user2)
		token2 = 'JWT ' + response.data.get('token', None)
		# set authentication token in header
		self.client.credentials(HTTP_AUTHORIZATION=token2)
		# test get while authenticated as user2
		response = self.client.get(
			'/bucketlists/' + str(bucketlist_id) + '/items/'
		)
		self.assertTrue(
			'You do not have permission to perform this action' in
			response.data.get('detail')
		)
		self.assertEqual(response.status_text, 'Forbidden')
		self.assertEqual(response.status_code, 403)

	def test_post_bucketlist_item_other_user(self):
		"""Test post operation on '/bucketlists/<buck_id>/items/' url when
		bucketlist has been created by a different user.
		"""
		# create user 1
		self.create_user(self.user1)
		# login user 1
		response = self.client.post('/auth/login/', self.user1)
		token1 = 'JWT ' + response.data.get('token', None)
		# set authentication token in header
		self.client.credentials(HTTP_AUTHORIZATION=token1)
		# create bucketlist
		bucketlist = {
			'name': self.fake.name()
		}
		self.client.post('/bucketlists/', bucketlist)
		# send get request to /bucketlists/ and then retrieve bucketlist id
		response = self.client.get('/bucketlists/')
		results_list = response.data.get('results')
		bucketlist_id = results_list[0].get('buck_id')
		# clear user1 credentials
		self.client.credentials()
		# create user 2
		user2 = {
			'username': self.fake.user_name(),
			'password': self.fake.password()
		}
		self.create_user(user2)
		# login user2
		response = self.client.post('/auth/login/', user2)
		token2 = 'JWT ' + response.data.get('token', None)
		# set authentication token in header
		self.client.credentials(HTTP_AUTHORIZATION=token2)
		# try to post item as user2 in self.user1's bucketlist
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
			'You do not have permission to perform this action.'
		)
		self.assertEqual(response.status_text, 'Forbidden')
		self.assertEqual(response.status_code, 403)

	def test_put_bucketlist_item_other_user(self):
		"""Test put operation on '/bucketlists/<buck_id>/items/<item_id>/' url
		when the bucketlist has been created by a different user.
		"""
		# create user 1
		self.create_user(self.user1)
		# login user 1
		response = self.client.post('/auth/login/', self.user1)
		token1 = 'JWT ' + response.data.get('token', None)
		# set authentication token in header
		self.client.credentials(HTTP_AUTHORIZATION=token1)
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
		# get the id of the new item in bucketlist
		response = self.client.get(
			'/bucketlists/' + str(bucketlist_id) + '/items/'
		)
		item_id = response.data[0].get('item_id')
		# remove user1 credentials
		self.client.credentials()

		# create user 2
		self.create_user(self.user2)
		# login user 2
		response = self.client.post('/auth/login/', self.user2)
		token2 = 'JWT ' + response.data.get('token', None)
		# set authentication token in header
		self.client.credentials(HTTP_AUTHORIZATION=token2)
		# test put while authenticated as user2
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
			'You do not have permission to perform this action.'
		)
		self.assertEqual(response.status_text, 'Forbidden')
		self.assertEqual(response.status_code, 403)

	def test_delete_bucketlist_item_other_user(self):
		"""Test delete operation on '/bucketlists/<buck_id>/items/<item_id>/' url
		when the bucketlist has been created by a different user."""
		# create user 1
		self.create_user(self.user1)
		# login user 1
		response = self.client.post('/auth/login/', self.user1)
		token1 = 'JWT ' + response.data.get('token', None)
		# set authentication token in header
		self.client.credentials(HTTP_AUTHORIZATION=token1)
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
		# get the id of the new item in bucketlist
		response = self.client.get(
			'/bucketlists/' + str(bucketlist_id) + '/items/'
		)
		item_id = response.data[0].get('item_id')
		# remove user1 credentials
		self.client.credentials()

		# create user 2
		self.create_user(self.user2)
		# login user 2
		response = self.client.post('/auth/login/', self.user2)
		token2 = 'JWT ' + response.data.get('token', None)
		# set authentication token in header
		self.client.credentials(HTTP_AUTHORIZATION=token2)
		# test delete while authenticated as user2
		response = self.client.delete(
			'/bucketlists/' + str(bucketlist_id) + '/items/' + str(item_id) + '/'
		)
		self.assertEqual(
			response.data.get('detail'),
			'You do not have permission to perform this action.'
		)
		self.assertEqual(response.status_text, 'Forbidden')
		self.assertEqual(response.status_code, 403)
