from test_base_class import TestBaseClass


class TestBucketListItemsId(TestBaseClass):

	def test_successful_put_bucketlist_items(self):
		"""Test successful put attempt on an item in a bucketlist."""
		# create the user
		self.create_user()
		# login the user
		self.client.post(
			'/auth/login',
			data={'username': self.username, 'password': self.password}
		)
		# create a buckelist
		bucketlist_name = self.fake.name()
		self.client.post(
			'/bucketlists/',
			data={'name': bucketlist_name}, headers={'username': token}
		)
		# create an item in the bucketlist
		item_name = self.fake.name()
		self.client.post(
			'/bucketlists/1',
			data={'name': item_name},
			headers={'username': token}
		)
		# update the item
		new_item_name = self.fake.name()
		self.client.post(
			'/bucketlists/1/items/1',
			data={'name': new_item_name},
			headers={'username': token}
		)

		self.assertTrue(new_item_name in response.content)
		self.assertFalse(item_name in response.content)
		self.assertEqual(response.status_code, 200)

	def test_unauthenticated_put_bucketlist_items(self):
		"""Test unauthenticated put attempt on an item in a bucketlist."""
		# create the user
		self.create_user()
		# login the user
		self.client.post(
			'/auth/login',
			data={'username': self.username, 'password': self.password}
		)
		# create a buckelist
		bucketlist_name = self.fake.name()
		self.client.post(
			'/bucketlists/',
			data={'name': bucketlist_name},
			headers={'username': token}
		)
		# create an item in the bucketlist
		item_name = self.fake.name()
		self.client.post(
			'/bucketlists/1',
			data={'name': item_name},
			headers={'username': token}
		)
		# update the item
		new_item_name = self.fake.name()
		self.client.post(
			'/bucketlists/1/items/1',
			data={'name': new_item_name}
		)

		self.assertTrue('Unauthorised access' in response.content)
		self.assertEqual(response.status_code, 403)

	def test_successful_delete_bucketlist_items(self):
		"""Test successful delete attempt on an item in a bucketlist."""
		# create the user
		self.create_user()
		# login the user
		self.client.post(
			'/auth/login',
			data={'username': self.username, 'password': self.password}
		)
		# create a buckelist
		bucketlist_name = self.fake.name()
		self.client.post(
			'/bucketlists/',
			data={'name': bucketlist_name},
			headers={'username': token}
		)
		# create an item in the bucketlist
		item_name = self.fake.name()
		self.client.post(
			'/bucketlists/1',
			data={'name': item_name},
			headers={'username': token}
		)
		# delete the item
		new_item_name = self.fake.name()
		self.client.post(
			'/bucketlists/1/items/1',
			data={'name': new_item_name},
			headers={'username': token}
		)

		self.assertTrue(
			'Item of id 1 in bucketlist of id 1 has been deleted'
			in response.content
		)
		self.assertEqual(response.status_code, 200)

		# attempt to delete non existent item
		new_item_name = self.fake.name()
		self.client.post(
			'/bucketlists/1/items/1',
			data={'name': new_item_name},
			headers={'username': token}
		)

		self.assertTrue('Resource not found' in response.content)
		self.assertEqual(response.status_code, 404)

	def test_unauthenticated_delete_bucketlist_items(self):
		"""Test unauthenticated delete attempt on an item in a bucketlist."""
		# create the user
		self.create_user()
		# login the user
		self.client.post(
			'/auth/login',
			data={'username': self.username, 'password': self.password}
		)
		# create a buckelist
		bucketlist_name = self.fake.name()
		self.client.post(
			'/bucketlists/',
			data={'name': bucketlist_name},
			headers={'username': token}
		)
		# create an item in the bucketlist
		item_name = self.fake.name()
		self.client.post(
			'/bucketlists/1',
			data={'name': item_name},
			headers={'username': token}
		)
		# delete the item
		new_item_name = self.fake.name()
		self.client.post(
			'/bucketlists/1/items/1',
			data={'name': new_item_name}
		)

		self.assertTrue('Unauthorised access' in response.content)
		self.assertEqual(response.status_code, 403)
