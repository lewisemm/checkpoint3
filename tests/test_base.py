
from rest_framework.test import APITestCase
from faker import Factory


class TestBaseClass(APITestCase):
	"""Parent class for all other tests."""

	def setUp(self):
		"""Initialize test resources."""
		self.fake = Factory.create()
		# self.client = Client()
		self.user1 = {
			'username': self.fake.user_name(),
			'password': self.fake.password()
		}
		self.user2 = {
			'username': self.fake.user_name(),
			'password': self.fake.password()
		}

	def tearDown(self):
		"""Free resources and do some housekeeping after tests are run."""
		del self.fake
		del self.client
		del self.user1
		del self.user2

	def create_user(self, user):
		"""Utility method to create a user by posting username and password
		info to '/users/' url.
		"""
		response = self.client.post(
			path='/users/',
			data=user,
			format='json'
		)
		return response
