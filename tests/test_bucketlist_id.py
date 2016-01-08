from test_base_class import TestBaseClass


class TestBucketListID(TestBaseClass):

	def test_successful_get_bucketlist_id(self):
		"""Test a successful get attempt of a bucketlist of the specified id."""
		# create a user
		self.create_user()
		# login user
		self.client.post(
			'/auth/login',
			{'username': self.username, 'password': self.password}
		)
		# create a bucketlist
		bucketlist_name = self.fake.name()
		self.client.post(
			'/bucketlists/',
			data={'name': bucketlist_name},
			headers={'username': token}
		)
		# the get request to bucketlist id 1
		response = self.client.get('/bucketlists/1', headers={'username': token})

		self.assertTrue(bucketlist_name in response.content)
		self.assertEqual(response.status_code, 200)

	def test_unauthenticated_get_bucketlist_id(self):
		"""Test an unauthenticated get attempt
			to retrieve the bucketlist of the specified id."""
		# create a user
		self.create_user()
		# login user
		self.client.post(
			'/auth/login',
			{'username': self.username, 'password': self.password}
		)
		# create a bucketlist
		bucketlist_name = self.fake.name()
		self.client.post(
			'/bucketlists/',
			data={'name': bucketlist_name},
			headers={'username': token}
		)
		# the get request to bucketlist id 1
		response = self.client.get('/bucketlists/1')

		self.assertTrue('Unauthorised access' in response.content)
		self.assertEqual(response.status_code, 403)

	def test_successful_put_bucketlist_id(self):
		"""Test a successful put attempt of a bucketlist of the specified id."""
		# create a user
		self.create_user()
		# login user
		self.client.post(
			'/auth/login',
			{'username': self.username, 'password': self.password}
		)
		# create a bucketlist
		bucketlist_name = self.fake.name()
		self.client.post(
			'/bucketlists/',
			data={'name': bucketlist_name},
			headers={'username': token}
		)
		# the put request to bucketlist id 1
		new_bucketlist_name = self.fake.name()
		response = self.client.get(
			'/bucketlists/1',
			data={'name': new_bucketlist_name},
			headers={'username': token}
		)

		self.assertTrue(new_bucketlist_name in response.content)
		self.assertEqual(response.status_code, 200)

	def test_unauthenticated_put_bucketlist_id(self):
		"""Test an unauthenticated put attempt
			to update the bucketlist of the specified id."""
		# create a user
		self.create_user()
		# login user
		self.client.post(
			'/auth/login',
			{'username': self.username, 'password': self.password}
		)
		# create a bucketlist
		bucketlist_name = self.fake.name()
		self.client.post(
			'/bucketlists/',
			data={'name': bucketlist_name},
			headers={'username': token}
		)
		# the put request to bucketlist id 1
		new_bucketlist_name = self.fake.name()
		response = self.client.get(
			'/bucketlists/1',
			data={'name': new_bucketlist_name}
		)

		self.assertTrue('Unauthorised access' in response.content)
		self.assertEqual(response.status_code, 403)

	def test_successful_delete_bucketlist_id(self):
		"""Test a successful delete attempt
			to the bucketlist of the specified id."""
		# create a user
		self.create_user()
		# login user
		self.client.post(
			'/auth/login',
			{'username': self.username, 'password': self.password}
		)
		# create a bucketlist
		bucketlist_name = self.fake.name()
		self.client.post(
			'/bucketlists/',
			data={'name': bucketlist_name},
			headers={'username': token}
		)
		# the delete request to bucketlist id 1
		response = self.client.delete(
			'/bucketlists/1',
			headers={'username': token}
		)

		self.assertTrue('Bucketlist of id 1 has been deleted' in response.content)
		self.assertEqual(response.status_code, 200)

	def test_unauthenticated_delete_bucketlist_id(self):
		"""Test a successful delete attempt
			of the bucketlist of the specified id."""
		# create a user
		self.create_user()
		# login user
		self.client.post(
			'/auth/login',
			{'username': self.username, 'password': self.password}
		)
		# create a bucketlist
		bucketlist_name = self.fake.name()
		self.client.post(
			'/bucketlists/',
			data={'name': bucketlist_name},
			headers={'username': token}
		)
		# the delete request to bucketlist id 1
		response = self.client.delete('/bucketlists/1')

		self.assertTrue('Unauthorised access' in response.content)
		self.assertEqual(response.status_code, 403)
