from test_base_class import TestBaseClass


class TestLogout(TestBaseClass):

	def login(self):
		"""Create a new user and log him/her in."""
		# create a user
		self.create_user()
		self.client.post(
			'/auth/login',
			{'username': self.username, 'password': self.password}
		)

	def test_successful_logout(self):
		"""Test the successful logout of a user who provides a token."""
		# user logs in
		self.login()
		# user logs out
		self.client.get(
			'/auth/logout',
			data={'username': token}
		)
		self.assertTrue('Successfully loggged out' in response.data)
		self.assertEqual('200' in response.status_code)

	def test_logout_without_token(self):
		"""Test the logout attempt without an authentication token."""
		# user logs in
		self.login()
		# user logs out
		self.client.get('/auth/logout')
		self.assertTrue('Authentication token not provided!' in response.data)
		self.assertEqual('400' in response.status_code)
