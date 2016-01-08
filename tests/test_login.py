from test_base_class import TestBaseClass


class TestLogin(TestBaseClass):
	"""This class tests the functionality of the login mechanism."""

	def test_successful_login(self):
		"""Create a new user and test successful login thereafter."""
		# create a user in the system first
		self.create_user()
		# test login with that user
		response = self.client.post(
			'/auth/login',
			{'username': self.username, 'password': self.password}
		)

		self.assertTrue('token' in response.data)
		self.assertEqual('200', response.status_code)

	def test_non_existent_user_login(self):
		"""Test login of a user who is not registered in the system."""
		# create arbitrary credentials
		username = self.fake.user_name()
		password = self.fake.password()
		# test login
		response = self.client.post(
			'/auth/login',
			{'username': username, 'password': password}
		)

		self.assertTrue('Username does not exist' in response.data)
		self.assertEqual('200', response.status_code)

	def test_login_missing_credentials(self):
		"""Test the validation of user input during attempted login."""
		username = self.fake.user_name()
		password = self.fake.password()

		# test login without username
		self.client.post('/auth/login', {'password': password})
		self.assertTrue('Username missing!' in response.data)

		# test login without password
		self.client.post('/auth/login', {'username': username})
		self.assertTrue('Password missing!' in response.data)

		# test login without either username or password
		self.client.post('/auth/login')
		self.assertTrue('User credentials missing!' in response.data)
