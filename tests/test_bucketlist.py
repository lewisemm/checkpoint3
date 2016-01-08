from test_base_class import TestBaseClass


class TestBucketList(TestBaseClass):

	def test_successful_create_bucketlist(self):
		"""Test successful creation of a bucketlist."""
		# create a user
		self.create_user()
		# log them in
		self.client.post(
			'/auth/login',
			{'username': self.username, 'password': self.password}
		)
		# create a bucketlist
		buck_name = self.fake.name()
		self.client.post(
			'/bucketlists/',
			data={'name': buck_name},
			headers={'username': token}
		)

		self.assertTrue(buck_name in response.content)
		self.assertEqual(response.status_code, 201)

	def test_unauthenticated_create_bucketlist(self):
		"""Test attempt to create a bucketlist without the authentication token."""
		# create a user
		self.create_user()
		# log them in
		self.client.post(
			'/auth/login',
			{'username': self.username, 'password': self.password}
		)
		# create a bucketlist
		buck_name = self.fake.name()
		self.client.post('/bucketlists/', data={'name': buck_name})

		self.assertTrue('Unauthoried accesss' in response.content)
		self.assertEqual(response.status_code, 403)

	def test_successful_authenticated_get_bucketlists(self):
		"""Test successful attempt to get bucketlists in the system."""
		# create a user
		self.create_user()
		# login user
		self.client.post(
			'/auth/login',
			{'username': self.username, 'password': self.password},
			headers={'username': token}
		)
		# create a bucketlist
		buck_name = self.fake.name()
		self.client.post(
			'/bucketlists/',
			data={'name': buck_name},
			headers={'username': token}
		)
		# create another bucketlist
		buck_name2 = self.fake.name()
		self.client.post(
			'/bucketlists/',
			data={'name': buck_name2},
			headers={'username': token}
		)
		# confirm the two bucketlists are there in the response
		self.assertTrue(buck_name in response.content)
		self.assertTrue(buck_name2 in response.content)

		self.assertEqual(response.status_code, 200)

	def test_unauthenticated_get_bucketlists(self):
		"""Test unauthenticated attempt to get bucketlists in the system."""
		# create a user
		self.create_user()
		# login user
		self.client.post(
			'/auth/login',
			{'username': self.username, 'password': self.password},
			headers={'username': token}
		)
		# create a bucketlist
		buck_name = self.fake.name()
		self.client.post('/bucketlists/', data={'name': buck_name})

		self.assertTrue('Unauthoried accesss' in response.content)
		self.assertEqual(response.status_code, 403)
