from test_base_class import TestBaseClass

class TestBucketListIDItems(TestBaseClass):

	def test_successful_post_bucketlist_items(self):
		"""
		Tests a successful attempt to create an item in a bucketlist.
		"""
		# create a user
		self.create_user()
		# login the user
		self.client.post('/auth/login', data={'username': self.username, 'password': self.password})
		# create a bucketlist
		bucketlist_name = self.fake.name()
		self.client.post('/bucketlists/', data={'name': bucketlist_name}, headers={'username': token})
		# create item in the bucketlist
		item_name = self.fake.name()
		response = self.client.post('/bucketlists/1', data={'name': item_name}, headers={'username': token})

		self.assertTrue(item_name in response.content)
		self.assertEqual(response.status_code, 201)

		# create another item in the bucketlist
		item_name2 = self.fake.name()
		response = self.client.post('/bucketlists/1', data={'name': item_name2}, headers={'username': token})

		self.assertTrue(item_name2 in response.content)
		self.assertFalse(item_name in response.content)
		self.assertEqual(response.status_code, 201)

	def test_unauthenticated_post_bucketlist_items(self):
		"""
		Tests unauthenticated attempt to create an item in a bucketlist.
		"""
		# create a user
		self.create_user()
		# login the user
		self.client.post('/auth/login', data={'username': self.username, 'password': self.password})
		# create a bucketlist
		bucketlist_name = self.fake.name()
		self.client.post('/bucketlists/', data={'name': bucketlist_name}, headers={'username': token})
		# attempt to create item in the bucketlist
		item_name = self.fake.name()
		response = self.client.post('/bucketlists/1', data={'name': item_name})

		self.assertTrue('Unauthorised access' in response.content)
		self.assertEqual(response.status_code, 403)

		# attempt to create another item in the bucketlist
		item_name2 = self.fake.name()
		response = self.client.post('/bucketlists/1', data={'name': item_name2})

		self.assertTrue('Unauthorised access' in response.content)
		self.assertEqual(response.status_code, 403)