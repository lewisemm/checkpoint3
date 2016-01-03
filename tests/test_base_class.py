from django.test import TestCase, Client
from faker import Factory

import models

class TestBaseClass(TestCase):

	def setUp(self):
		self.fake = Factory.create()
		self.client = Client()

	def tearDown(self):
		del self.fake
		del self.client
		del self.username
		del self.password

	def create_user(self):
		"""
		This method registers a new user for use in the tests below.
		"""
		self.username = self.fake.user_name()
		self.password = self.fake.password()

		self.client.post('/user/register', {'username': self.username, 'password': self.password})