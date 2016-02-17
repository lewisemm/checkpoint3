from .test_base import TestBaseClass

from api.models import BucketList


class TestBucketlist(TestBaseClass):
	"""Test all permissible http methods on bucketlists."""

	def test_successful_post_bucketlist(self):
		"""Test successful post operation on '/bucketlist/' url."""
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
		response = self.client.post('/bucketlists/', bucketlist)

		self.assertEqual(response.data.get('message'), 'BucketList created')
		self.assertEqual(response.status_code, 201)
		self.assertEqual(response.status_text, 'Created')
		# fetch object from DB and confirm created_by == currently logged in user
		bucketlist_obj = BucketList.objects.get(name=bucketlist.get('name'))
		self.assertEqual(bucketlist_obj.created_by, self.user1.get('username'))

	def test_successful_get_bucketlist(self):
		"""Test successful get operation on '/bucketlist/' url."""
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
		# send get request to /bucketlists/
		response = self.client.get('/bucketlists/')
		self.assertTrue(len(response.data.get('results')), 1)
		results_list = response.data.get('results')
		self.assertEqual(results_list[0].get('name'), bucketlist.get('name'))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.status_text, 'OK')

	def test_successful_get_bucketlist_query_string_search(self):
		"""Test successful get operation on '/bucketlist/' url when query string
		is provided.
		"""
		# create user
		self.create_user(self.user1)
		# login user
		response = self.client.post('/auth/login/', self.user1)
		token = 'JWT ' + response.data.get('token', None)
		# set authentication token in header
		self.client.credentials(HTTP_AUTHORIZATION=token)
		# create bucketlist
		bucketlist = {
			'name': self.fake.name()
		}
		self.client.post('/bucketlists/', bucketlist)
		# send get request to /bucketlists/ with a query string
		response = self.client.get('/bucketlists/?q=' + bucketlist.get('name'))
		self.assertEqual(
			response.data.get('results')[0].get('name'), bucketlist.get('name')
		)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.status_text, 'OK')

	def test_successful_get_one_bucketlist(self):
		"""Test successful get operation on '/bucketlist/<buck_id>/' url."""
		# create user
		self.create_user(self.user1)
		# login user
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
		# append the id of the just created bucketlist to the url
		response = self.client.get('/bucketlists/' + str(bucketlist_id) + '/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.status_text, 'OK')
		self.assertEqual(response.data.get('name'), bucketlist.get('name'))
		self.assertEqual(response.data.get('created_by'), self.user1.get('username'))

	def test_successful_put_bucketlist(self):
		"""Test successful put operation on '/bucketlist/<buck_id>' url."""
		# create user
		self.create_user(self.user1)
		# login user
		response = self.client.post('/auth/login/', self.user1)
		token = 'JWT ' + response.data.get('token', None)
		# set authentication token in header
		self.client.credentials(HTTP_AUTHORIZATION=token)
		# create bucketlist
		bucketlist = {
			'name': self.fake.name()
		}
		self.client.post('/bucketlists/', bucketlist)
		# send a get request to /bucketlists/ to retrieve the bucketlist's id
		response = self.client.get('/bucketlists/')
		results_list = response.data.get('results')
		bucketlist_id = results_list[0].get('buck_id')
		# append the id of the bucketlist that's just been created to the url
		# to edit it
		new_data = {
			'name': self.fake.name()
		}
		response = self.client.put(
			'/bucketlists/' + str(bucketlist_id) + '/',
			new_data
		)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.status_text, 'OK')
		self.assertEqual(response.data.get('name'), new_data.get('name'))
		self.assertNotEqual(response.data.get('name'), bucketlist.get('username'))

	def test_successful_delete_bucketlist(self):
		"""Test successful delete operation on '/bucketlist/<buck_id>/' url."""
		# create user
		self.create_user(self.user1)
		# login user
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
		# append id of bucketlist just created to the url
		response = self.client.delete('/bucketlists/' + str(bucketlist_id) + '/')
		self.assertEqual(response.status_code, 204)
		self.assertEqual(response.status_text, 'No Content')
		# send a get to url of this bucketlist id to confirm success of delete
		# operation
		response = self.client.get('/bucketlists/' + str(bucketlist_id) + '/')
		self.assertEqual(response.data.get('detail'), 'Not found.')
		self.assertEqual(response.status_code, 404)
		self.assertEqual(response.status_text, 'Not Found')

	def test_unauthenticated_get_bucketlist(self):
		"""Test unauthenticated get operation on '/bucketlist/' url.

		Access should be denied because this is a protected route.
		"""
		# create user
		self.create_user(self.user1)
		# login user
		response = self.client.post('/auth/login/', self.user1)
		token = 'JWT ' + response.data.get('token', None)
		# set authentication token in header
		self.client.credentials(HTTP_AUTHORIZATION=token)
		# create bucketlist
		bucketlist = {
			'name': self.fake.name()
		}
		self.client.post('/bucketlists/', bucketlist)
		# clear authentication credentials
		self.client.credentials()
		# send get request to /bucketlists/
		response = self.client.get('/bucketlists/')
		self.assertTrue(
			'credentials were not provided' in response.data.get('detail')
		)
		self.assertEqual(response.status_code, 401)
		self.assertEqual(response.status_text, 'Unauthorized')

	def test_unauthenticated_get_one_bucketlist(self):
		"""Test unauthenticated get operation on '/bucketlist/<buck_id>/' url.

		Access should be denied because this is a protected route.
		"""
		# create user
		self.create_user(self.user1)
		# login user
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
		# clear authentication credentials
		self.client.credentials()
		# append id of the bucketlist that's just been created to the url
		response = self.client.get('/bucketlists/' + str(bucketlist_id) + '/')
		self.assertEqual(response.status_code, 401)
		self.assertEqual(response.status_text, 'Unauthorized')
		self.assertTrue(
			'credentials were not provided' in response.data.get('detail')
		)

	def test_unauthenticated_post_bucketlist(self):
		"""Test unauthenticated post operation on '/bucketlist/' url.

		(Unauthorized errors expected)
		"""
		# create bucketlist without authorization token
		bucketlist = {
			'name': self.fake.name()
		}
		response = self.client.post('/bucketlists/', bucketlist)
		self.assertEqual(
			response.data.get('detail'),
			'Authentication credentials were not provided.'
		)
		self.assertEqual(response.status_code, 401)
		self.assertEqual(response.status_text, 'Unauthorized')

	def test_unauthenticated_put_bucketlist(self):
		"""Test unauthenticated put operation on '/bucketlist/<buck_id>/' url."""
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
		# clear authentication credentials
		self.client.credentials()
		# append id of the bucketlist that's just been created to the url
		new_data = {
			'name': self.fake.name()
		}
		response = self.client.put(
			'/bucketlists/' + str(bucketlist_id) + '/',
			new_data
		)
		self.assertEqual(response.status_code, 401)
		self.assertEqual(response.status_text, 'Unauthorized')
		self.assertEqual(
			response.data.get('detail'),
			'Authentication credentials were not provided.'
		)

	def test_unauthenticated_delete_bucketlist(self):
		"""Test unauthenticated delete operation on '/bucketlist/<buck_id>/' url."""
		# create user
		self.create_user(self.user1)
		# login user
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
		# reset credentials
		self.client.credentials()
		# append if of bucketlist just created and attempt a delete
		response = self.client.delete('/bucketlists/' + str(bucketlist_id) + '/')
		self.assertEqual(response.status_code, 401)
		self.assertEqual(response.status_text, 'Unauthorized')
		self.assertEqual(
			response.data.get('detail'),
			'Authentication credentials were not provided.'
		)
